from config.config import PRE_FUSION_TOPICS


class TopicObject(object):
    def __init__(self, topic):
        self._messages = [[]]
        self._topic = topic
        self._is_utm = True if 'utm' in topic else False
        self._is_detection = True if 'detection' in topic else False
        self._is_pre_fusion = True if topic in PRE_FUSION_TOPICS else False

    def get_by_index(self, index):
        try:
            return self._messages[index]
        except:
            return self._messages[-1]

    def get_messages(self):
        return self._messages

    def is_utm(self):
        return self._is_utm

    def is_detection(self):
        return self._is_detection

    def is_prefusion(self):
        return self._is_pre_fusion

    def topic(self):
        return self._topic

    def __len__(self):
        return len(self._messages)
