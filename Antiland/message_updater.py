import json
import aiohttp
from datetime import datetime

async def handle_response(response, expected_status_code):
    error_message = await response.text()
    if "My rude words were blocked." in error_message:
        print("Message Blocked For Innapropriate Language")
    if "Message blocked." in error_message:
        print("Message Blocked For Personal Data")
    if response.status != expected_status_code:
        print(f"Request failed with status code {response.status}: {error_message}")
        # You can raise an exception here or handle the error as needed.
    else:
        pass  # Assuming the response is JSON

class MessageUpdater:
    previous_message_text = None

    def __init__(self, url, username, callback,selfbot):
        self.url = url
        self.username = username
        self.callback = callback
        self.running = False
        self.session = None
        self.selfbot=selfbot

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
        self.selfbot=selfbot
        previous_message_text = None
        async with aiohttp.ClientSession() as session:
            self.session = session
            while self.running:
                json_response = await self.fetch_messages()
                if json_response:
                    message_text = self.extract_message_text(json_response)
                    message_sender = self.extract_message_sender(json_response)
                    # Check the selfbot flag directly
                    if not self.selfbot:  # Respond to all messages
                        if message_text and message_text != previous_message_text:
                            previous_message_text = message_text
                            await self.callback(message_text, message_sender)
                    elif self.selfbot:  # Respond only to messages from the logged-in user
                        if message_text and message_text != previous_message_text and message_sender == self.username:
                            previous_message_text = message_text
                            await self.callback(message_text, message_sender)


    def extract_message_text(self, json_response):
        messages = json_response.get("m", [])
        if messages:
            last_message = messages[-1]
            message_text = last_message.get("d", {}).get("message")
            return message_text
        return None

    def extract_message_sender(self, json_response):
        messages = json_response.get("m", [])
        if messages:
            last_message = messages[-1]
            message_sender = last_message.get("d", {}).get("sendersName")
            return message_sender
        return None

    async def start(self):
        await self.run()

    def stop(self):
        self.running = False