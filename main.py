from time import sleep
from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from config.config import KAFKA_HOST, KAFKA_PORT, KAFKA_CONSUME_TOPICS


class Main(object):
    def __init__(self, host, port, topics):
        self.running = True
        self.kafka_host = host
        self.kafka_port = port
        self.kafka_topics = topics
        self.consumer = None

    def start(self):
        print(f"Starting Kafka consumer")
        self.consumer = KafkaConsumer(bootstrap_servers=f'{self.kafka_host}:{self.kafka_port}',
                                      auto_offset_reset='earliest',
                                      consumer_timeout_ms=1000)
        self.consumer.subscribe(self.kafka_topics)

    def run(self):
        while self.running:
            self.topics_messages_count()
            sleep(1)

    def topics_messages_count(self):
        for topic in self.kafka_topics:
            print(f"{topic} has {self.topic_messages_count(topic)} messages")

    def topic_messages_count(self, topic):
        partitions = self.topic_partitions_count(topic)
        topic_messages = 0
        if not partitions:
            return 0
        for partition in partitions:
            topic_messages += self.partition_messages_count(topic, partition)
        return topic_messages

    def topic_partitions_count(self, topic):
        return list(self.consumer.partitions_for_topic(topic))

    def partition_messages_count(self, topic, partition_id):
        topic_partition = [TopicPartition(topic, partition_id)]
        beginning_offset = self.consumer.beginning_offsets(topic_partition)
        end_offset = self.consumer.end_offsets(topic_partition)
        return end_offset[topic_partition[0]] - beginning_offset[topic_partition[0]]

    def stop(self):
        self.running = False
        self.consumer.close()


if __name__ == '__main__':
    main = Main(host=KAFKA_HOST, port=KAFKA_PORT, topics=KAFKA_CONSUME_TOPICS)
    main.start()
    main.run()
