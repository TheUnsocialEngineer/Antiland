class Message:
    """
    Represents a message in the Antiland platform.

    Args:
        data (dict): The message data.

    Attributes:
        _data (dict): The raw data of the message.

    Properties:
        id (str): The ID of the message.
        text (str): The content of the message.
        sender_id (str): The ID of the message sender.
        dialogue_id (str): The ID of the dialogue associated with the message.

    Example:
        >>> message_data = {
        ...     "objectId": "123456",
        ...     "message": "Hello, world!",
        ...     "senderId": "user123",
        ...     "dialogue": "dialogue789"
        ... }
        >>> message = Message(message_data)
        >>> message.id
        '123456'
        >>> message.text
        'Hello, world!'
        >>> message.sender_id
        'user123'
        >>> message.dialogue_id
        'dialogue789'
    """
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