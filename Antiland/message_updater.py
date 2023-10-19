import json
import aiohttp
from datetime import datetime

class Message:
    def __init__(self, message_data):
        self.text = message_data.get("d", {}).get("message")
        self.sender_id = message_data.get("d", {}).get("senderId")
        self.sender_name = message_data.get("d", {}).get("sendersName")

class MessageUpdater:
    def __init__(self, url, username, selfbot=False):
        self.url = url
        self.username = username
        self.selfbot = selfbot
        self.running = False
        self.session = None
        self.previous_message_text = None
    
    async def handle_response(self, response, expected_status_code):
        error_message = await response
        if "My rude words were blocked." in error_message:
            print("Message Blocked For Inappropriate Language")
        if "Message blocked." in error_message:
            print("Message Blocked For Personal Data")
        if response.status != expected_status_code:
            print(f"Request failed with status code {response.status}: {error_message}")
            # You can raise an exception here or handle the error as needed.
        else:
            pass  # Assuming the response is JSON

    async def fetch_messages(self):
        async with self.session.get(self.url) as response:
            if response.status == 200:
                content_type = response.headers.get('Content-Type', '').lower()
                if 'application/json' in content_type or 'text/javascript' in content_type:
                    try:
                        response_text = await response.text()
                        json_response = json.loads(response_text)
                        return json_response
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                else:
                    print(f"Received unexpected content type: {content_type}")
            return None

    async def run(self,selfbot):
        self.running = True
        previous_message_text = None
        self.selfbot=selfbot
        async with aiohttp.ClientSession() as session:
            self.session = session
            while self.running:
                json_response = await self.fetch_messages()
                if json_response:
                    messages_data = json_response.get("m", [])
                    messages = [Message(message_data) for message_data in messages_data]
                    last_message=messages[-1]
                    message_text = last_message.text
                    message_sender = last_message.sender_name
                    # Check the selfbot flag directly
                    if not self.selfbot:  # Respond to all messages
                        if message_text and message_text != previous_message_text:
                            previous_message_text = message_text
                            await self.callback(last_message)
                    elif self.selfbot:  # Respond only to messages from the logged-in user
                        if message_text and message_text != previous_message_text and message_sender == self.username:
                            previous_message_text = message_text
                            await self.callback(last_message)

    async def start(self):
        await self.run()

    def stop(self):
        self.running = False

    async def callback(self,message):
        # Implement your callback logic here
        return(message)