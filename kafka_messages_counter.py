from kafka import KafkaConsumer
from kafka.structs import TopicPartition


class KafkaMessagesCounter(object):
    def __init__(self, host, port, topics):
        self._running = True
        self._kafka_host = host
        self._kafka_port = port
        self._kafka_topics = topics
        self._consumer = None

    def _start(self):
        self._consumer = KafkaConsumer(bootstrap_servers=f'{self._kafka_host}:{self._kafka_port}',
                                       auto_offset_reset='earliest',
                                       consumer_timeout_ms=1000)
        self._consumer.subscribe(self._kafka_topics)

    def topics_messages_count(self):
        res = []
        self._start()
        for topic in self._kafka_topics:
            r = self._topic_messages_count(topic)
            res.append(r)
        self._stop()
        return res

    def _topic_messages_count(self, topic):
        partitions = self._topic_partitions_count(topic)
        topic_messages = 0
        if not partitions:
            return 0
        for partition in partitions:
            topic_messages += self._partition_messages_count(topic, partition)
        return topic_messages

    def _topic_partitions_count(self, topic):
        return list(self._consumer.partitions_for_topic(topic))

    def _partition_messages_count(self, topic, partition_id):
        topic_partition = [TopicPartition(topic, partition_id)]
        beginning_offset = self._consumer.beginning_offsets(topic_partition)
        end_offset = self._consumer.end_offsets(topic_partition)
        return end_offset[topic_partition[0]] - beginning_offset[topic_partition[0]]

    def _stop(self):
        self._running = False
        self._consumer.close()
