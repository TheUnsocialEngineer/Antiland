class Message:
    def __init__(self, data):
        self._data = data

    @property
    def id(self):
        return self._data["objectId"]

    @property
    def text(self):
        return self._data["message"]

    @property
    def sender_id(self):
        return self._data["senderId"]

    @property
    def dialogue_id(self):
        return self._data["dialogue"]