from kafka import KafkaConsumer

KAFKA_CONSUME_TOPIC = 'dummycontrol'
KAFKA_HOST = '152.66.93.23'
KAFKA_PORT = '9092'

consumer = KafkaConsumer(KAFKA_CONSUME_TOPIC, bootstrap_servers=f'{KAFKA_HOST}:{KAFKA_PORT}', consumer_timeout_ms=1000)
print(f'Kafka server: "{KAFKA_CONSUME_TOPIC}" topic has partitions: {consumer.partitions_for_topic(KAFKA_CONSUME_TOPIC)}')
consumer.seek_to_beginning()
consumer.poll()

messages = []
for msg in consumer:
    print("%s:%d:%d: key=%s value=%s" % (msg.topic, msg.partition, msg.offset, msg.key, msg.value))
    messages.append(msg.value)

consumer.close()

print(f'{len(messages)} messages retrieved.')
