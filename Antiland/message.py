class Message:
    def __init__(self, data):
        self.id = data["objectId"]
        self.text = data["message"]
        self.sender_id = data["senderId"]
        self.dialogue_id = data["dialogue"]