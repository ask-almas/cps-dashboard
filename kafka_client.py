import time
import math

from kafka import KafkaConsumer
from kafka.structs import TopicPartition

from config.config import KAFKA_PORT, KAFKA_HOST, KAFKA_CONSUME_TOPICS, SENSORIS_WGS_RESOLUTION, FUSION_SSID
from gps_object import GPSObject
from sensoris.protobuf.messages.data_pb2 import DataMessage


class KafkaClient(object):
    def __init__(self):
        self._kafka_host = KAFKA_HOST
        self._kafka_port = KAFKA_PORT
        self._kafka_topics = KAFKA_CONSUME_TOPICS
        self._consumer = None

    def get_topic_options(self):
        count = self.count_messages_in_topics()
        res = []
        for i, t in enumerate(self._kafka_topics):
            res.append({"label": f"{t}: {count[i]} messages available", "value": t})
        return res

    def count_messages_in_topics(self):
        res = []
        self._subscribe_for_topics()
        for topic in self._kafka_topics:
            r = self._count_messages_in_topic(topic)
            res.append(r)
        self._stop()
        return res

    def _subscribe_for_topics(self):
        self._consumer = KafkaConsumer(bootstrap_servers=f'{self._kafka_host}:{self._kafka_port}',
                                       auto_offset_reset='earliest',
                                       consumer_timeout_ms=1000)
        self._consumer.subscribe(self._kafka_topics)

    def _count_messages_in_topic(self, topic):
        partitions = self._count_topic_partitions(topic)
        topic_messages = 0
        if not partitions:
            return 0
        for partition in partitions:
            topic_messages += self._count_messages_in_partition(topic, partition)
        return topic_messages

    def _count_topic_partitions(self, topic):
        return list(self._consumer.partitions_for_topic(topic))

    def _count_messages_in_partition(self, topic, partition_id):
        topic_partition = [TopicPartition(topic, partition_id)]
        beginning_offset = self._consumer.beginning_offsets(topic_partition)
        end_offset = self._consumer.end_offsets(topic_partition)
        return end_offset[topic_partition[0]] - beginning_offset[topic_partition[0]]

    def _stop(self):
        self._consumer.close()

    def get_messages_from_topic(self, topic_ob=None):
        topic, is_utm, is_detection = topic_ob.topic(), topic_ob.is_utm(), topic_ob.is_detection()
        tic = time.perf_counter()
        print(f"Retrieving messages from topic: {topic}")
        self._connect_to_topic(topic)
        objects_list = topic_ob.get_messages()
        self._consumer.poll()
        d = {}
        pre_fusion = topic_ob.is_prefusion()
        c = 0
        for msg in self._consumer:
            if c == 10:
                time.sleep(0.01)
                c = 0
            c += 1
            dm = DataMessage()
            dm.ParseFromString(msg.value)
            objects = self._gps_objects_from(dm, is_utm, is_detection)
            if pre_fusion:
                if objects[0].ssid in d:
                    objects_list.append([])
                    d = {}
                else:
                    d[objects[0].ssid] = objects[0].ssid
                objects_list[-1].extend(objects)
            else:
                objects_list[-1].extend(objects)
                if objects[0].ssid == FUSION_SSID:
                    objects_list.append([])
        self._stop()
        toc = time.perf_counter()
        print(f"Messages updated in {toc - tic:0.4f} seconds")
        return objects_list

    def _connect_to_topic(self, topic):
        self._consumer = KafkaConsumer(topic,
                                       bootstrap_servers=f'{self._kafka_host}:{self._kafka_port}')
        print(f"Kafka {topic} topic has partitions: {self._consumer.partitions_for_topic(topic)}")
        self._consumer.seek_to_beginning()

    def _gps_objects_from(self, dm, utm=False, is_detection=False):
        result = []
        ssid = dm.envelope.ids.vehicle_id.value
        origin = dm.event_group[0].envelope.origin
        origin_ts = origin.timestamp.posix_time.value
        if utm:
            origin_gps = origin.position_and_accuracy.metric_ecef
        else:
            origin_gps = origin.position_and_accuracy.geographic_wgs84
        origin_lat, origin_lon, origin_alt = self._unpack_gps(origin_gps, utm)
        yaw = origin.orientation_and_accuracy.euler_vehicle.yaw.value/100
        origin = GPSObject(ssid, -1, origin_ts, origin_lat, origin_lon, origin_alt)
        result.append(origin)
        movable_objects = dm.event_group[0].object_detection_category.movable_object
        for mov in movable_objects:
            movobj_id = mov.object_id.value
            movobj_conf = mov.existence_confidence.value / 100.0
            box = mov.rectangular_box_and_accuracy.center_orientation_size
            if is_detection:
                box_gps = box.center_position_and_accuracy.metric_vehicle
            elif utm:
                box_gps = box.center_position_and_accuracy.metric_ecef
            else:
                box_gps = box.center_position_and_accuracy.geographic_wgs84
            box_lat, box_lon, box_alt = self._unpack_gps(box_gps, utm, is_detection,
                                                         origin_lat, origin_lon, origin_alt, yaw)
            cov_xx = box.center_position_and_accuracy.covariance.a11.value / 1000.0
            cov_yy = box.center_position_and_accuracy.covariance.a22.value / 1000.0
            cov_xy = box.center_position_and_accuracy.covariance.a12.value / 1000.0
            movobj = GPSObject(ssid, movobj_id, origin_ts, box_lat, box_lon, box_alt, movobj_conf, cov_xx, cov_yy,
                               cov_xy)
            result.append(movobj)
        return result

    @staticmethod
    def _unpack_gps(sensoris_gps_pos, utm=False, is_detection=False, origin_lat=0.0, origin_lon=0.0, origin_alt=0.0,
                    yaw=0.0):
        if is_detection and utm:
            x_hat = sensoris_gps_pos.x.value / 1000.0
            y_hat = sensoris_gps_pos.y.value / 1000.0
            lat = origin_lat + x_hat*math.sin(math.radians(yaw)) + y_hat*math.cos(math.radians(yaw))
            lon = origin_lon + x_hat*math.cos(math.radians(yaw)) - y_hat*math.sin(math.radians(yaw))
            alt = sensoris_gps_pos.z.value / 1000.0
        elif is_detection:
            x_hat = sensoris_gps_pos.x.value / 1000.0
            y_hat = sensoris_gps_pos.y.value / 1000.0
            d_x = x_hat*math.cos(math.radians(yaw)) - y_hat*math.sin(math.radians(yaw))
            d_y = x_hat*math.sin(math.radians(yaw)) + y_hat*math.cos(math.radians(yaw))
            lat = origin_lat + (d_y/6371000.0)*(180/math.pi)
            lon = origin_lon + (d_x/6371000.0)*(180/math.pi)/math.cos(origin_lat*math.pi/180)
            alt = sensoris_gps_pos.z.value / 1000.0
        elif utm:
            lat = sensoris_gps_pos.y.value / 1000.0
            lon = sensoris_gps_pos.x.value / 1000.0
            alt = sensoris_gps_pos.z.value / 1000.0
        else:
            lat = sensoris_gps_pos.latitude.value * SENSORIS_WGS_RESOLUTION
            lon = sensoris_gps_pos.longitude.value * SENSORIS_WGS_RESOLUTION
            alt = sensoris_gps_pos.altitude.value / 1000.0
        return lat, lon, alt
