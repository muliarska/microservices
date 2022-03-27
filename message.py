import uuid


class Message:
    def __init__(self, text):
        self._text = text
        self._uuid = str(uuid.uuid1())

    def text(self):
        return self._text

    def uuid(self):
        return self._uuid
