import threading
from kafka_client import KafkaClient


class ObjectListsThread(threading.Thread):
    def __init__(self, topic_ob):
        threading.Thread.__init__(self)
        self._topic_ob = topic_ob

    def run(self):
        kafka_client = KafkaClient()
        kafka_client.get_messages_from_topic(self._topic_ob)
