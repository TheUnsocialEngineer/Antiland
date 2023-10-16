import aiohttp
import base64
from Antiland.message import Message

class Dialogue:
    """
    Represents a dialogue or chat conversation within the Antiland application.

    Attributes:
        lang (str): The language of the dialogue.
        groupAdmins (list): List of group administrators' data.
        lastmessage (str): The last message in the dialogue.
        objectId (str): The unique identifier for the dialogue.
        guestname (str): The guest's name in the dialogue.
        foundername (str): The founder's name.
        founderId (str): The unique identifier of the founder.
        private (bool): Indicates if the dialogue is private.
        public (bool): Indicates if the dialogue is public.
        humanLink (str): A human-readable link associated with the dialogue.
        accepted (bool): Indicates if the dialogue has been accepted.
        flags (str): Flags associated with the dialogue.

    Methods:
        like_message(messageid, senderid, token, dialogue):
            Like a specific message in the dialogue.
        send_message(message, token=None, dialogue=None):
            Send a message to the dialogue.
        send_video(filepath, token, dialogue):
            Send a video message to the dialogue.
        send_image(filepath, token=None, dialogue=None):
            Send an image message to the dialogue.
        get_messages(chatid, token):
            Get a list of messages in the dialogue.
        add_mod(uuid, dialogue, token):
            Add a moderator to the dialogue.
        remove_mod(uuid, dialogue, token):
            Remove a moderator from the dialogue.

    Args:
        data (dict): A dictionary containing dialogue-related data.

    Note:
        The methods in this class use asynchronous I/O operations and should be awaited.
    """
    def __init__(self, data):
        self._data = data

    @property
    def lang(self):
        return self._data.get("lang")

    @property
    def groupAdmins(self):
        return self._data.get("groupAdmins")

    @property
    def lastmessage(self):
        return self._data["lastmessage"]

    @property
    def objectId(self):
        return self._data["objectId"]

    @property
    def guestname(self):
        return self._data.get("guestname")

    @property
    def foundername(self):
        return self._data["foundername"]

    @property
    def founderId(self):
        return self._data["founderId"]

    @property
    def private(self):
        return self._data.get("private")

    @property
    def public(self):
        return self._data.get("public")

    @property
    def humanLink(self):
        return self._data.get("humanLink")

    @property
    def accepted(self):
        return self._data.get("accepted")

    @property
    def flags(self):
        return self._data.get("flags")

    async def like_message(self, messageid, senderid, token, dialogue):
        url = "https://www.antichat.me/uat/parse/functions/loveMessage"
        json_payload = {
            "messageId": messageid,
            "dialogueId": dialogue,
            "senderId": senderid,
            "v": 10001,
            "_ApplicationId": "VxfAeNw8Vuw2XKCN",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "23b9f34b-a753-e248-b7c2-c80e38bc3b40",
            "_SessionToken": token
        }

        async with aiohttp.ClientSession() as session:
            await session.post(url, json=json_payload)

    async def send_message(self, message, token=None, dialogue=None):
        url = "https://mobile-elb.antich.at/classes/Messages"

        json_payload = {
            "receiver": "group",
            "dialogue": dialogue,
            "message": f"{message}",
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                await session.post(url, json=json_payload)

        except aiohttp.ClientError as client_error:
            print(f"Aiohttp ClientError: {client_error}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


    async def send_video(self, filepath, token, dialogue):
        # Convert backslashes to forward slashes in the file path
        filepath = filepath.replace("\\", "/")

        try:
            with open(filepath, 'rb') as image_file:
                data = base64.b64encode(image_file.read()).decode("utf-8")

            url = "https://mobile-elb.antich.at/files/upload.mp4"
            url2 = "https://mobile-elb.antich.at/classes/Messages"

            json_payload = {
                "base64": data,
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
                "_SessionToken": token
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as response:
                    if response.status != 200:
                        print(f"Request for uploading video failed with status code {response.status}.")
                        return

                    jsoner = await response.json()

            url = jsoner["url"]
            name = jsoner["name"]
            json_payload2 = {
                "dialogue": dialogue,
                "message": "[video]",
                "photo": {
                    "name": name,
                    "url": url,
                    "__type": "File"
                },
                "receiver": "group",
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
                "_SessionToken": token
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url2, json=json_payload2) as response:
                    if response.status != 201:
                        print(f"Request for sending video message failed with status code {response.status}.")
                        return

                    print(await response.text())
        except Exception as e:
            print(f"Error: {e}")

    async def send_image(self, filepath, token=None, dialogue=None):
        # Convert backslashes to forward slashes in the file path
        try:
            filepath = filepath.replace("\\", "/")
        except:
            pass

        try:
            with open(filepath, 'rb') as image_file:
                data = base64.b64encode(image_file.read()).decode("utf-8")

            url = "https://mobile-elb.antich.at/files/upload.jpg"
            url2 = "https://mobile-elb.antich.at/classes/Messages"

            json_payload = {
                "base64": data,
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
                "_SessionToken": token
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as response:
                    if response.status != 201:
                        print(f"Request for uploading image failed with status code {response.status}.")

                    jsoner = await response.json()

            url = jsoner["url"]
            name = jsoner["name"]

            json_payload2 = {
                "dialogue": dialogue,
                "message": "[photo]",
                "photo": {
                    "name": name,
                    "url": url,
                    "__type": "File"
                },
                "receiver": "group",
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
                "_SessionToken": token
            }

            async with aiohttp.ClientSession() as session:
                async with session.post(url2, json=json_payload2) as response:
                    if response.status != 201:
                        print(f"Request for sending image message failed with status code {response.status}.")
                        return
        except Exception as e:
            print(f"Error: {e}")

    async def get_messages(self, chatid, token):
        url = "https://mobile-elb.antich.at/functions/getMessagesAndRemoves"
        json_payload = {
            "dialogueId": chatid,
            "laterThan": {
                "iso": "2023-09-05T05:33:54.792Z",
                "__type": "Date"
            },
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as response:
                    if response.status != 200:
                        print(f"Request for getting messages failed with status code {response.status}.")
                        return []

                    data = await response.json()
                    messages_data = data["result"]["messages"]
                    messages = [Message(message_data) for message_data in messages_data]
                    return messages
        except Exception as e:
            print(f"Error: {e}")
            return []

    async def add_mod(self, uuid, dialogue, token):
        url = "https://mobile-elb.antich.at/functions/addMod"
        json_payload = {
            "modId": uuid,
            "dialogue": dialogue,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as response:
                    print(await response.text())
                    if response.status != 200:
                        print(f"Request for adding mod failed with status code {response.status}.")
        except Exception as e:
            print(f"Error: {e}")

    async def remove_mod(self, uuid, dialogue, token):
        url = "https://mobile-elb.antich.at/functions/removeMod"
        json_payload = {
            "modId": uuid,
            "dialogue": dialogue,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as response:
                    if response.status != 200:
                        print(f"Request for removing mod failed with status code {response.status}.")
        except Exception as e:
            print(f"Error: {e}")