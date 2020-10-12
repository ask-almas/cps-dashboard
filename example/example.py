from kafka import KafkaConsumer
from kafka.structs import TopicPartition
from config import KAFKA_PORT, KAFKA_HOST

KAFKA_CONSUME_TOPIC = "dummycontrol"

consumer = KafkaConsumer(KAFKA_CONSUME_TOPIC,
                         bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}',
                         auto_offset_reset='earliest',
                         consumer_timeout_ms=1000)
print(f'Kafka server: "{KAFKA_CONSUME_TOPIC}" topic has partitions: {consumer.partitions_for_topic(KAFKA_CONSUME_TOPIC)}')
a = [TopicPartition(KAFKA_CONSUME_TOPIC, 0)]
b = consumer.beginning_offsets(a)
e = consumer.end_offsets(a)
print(e[a[0]]-b[a[0]])

messages = []
for msg in consumer:
    # print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))
    messages.append(msg.value)

consumer.close()

print(f'{len(messages)} messages retrieved.')
