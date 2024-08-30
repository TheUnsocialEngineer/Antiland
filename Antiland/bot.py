import aiohttp
from Antiland.message_updater import MessageUpdater
from Antiland.dialogue import Dialogue
from Antiland.account import Account
from Antiland.user import User
import asyncio
from requests.structures import CaseInsensitiveDict

class Bot:
    """
    
    The `Bot` class represents a bot on the Antiland platform.

    Args:
        prefix (str): The command prefix to trigger bot commands.
        dialogue (str): The ID of the dialogue associated with the bot.
        session_token (str, optional): The session token for authentication. Defaults to None.

    Attributes:
        prefix (str): The command prefix to trigger bot commands.
        running (bool): A flag to indicate if the bot is running.
        session_token (str): The session token for authentication.
        message_updater (MessageUpdater): An instance of the MessageUpdater class.
        dialogue (str): The ID of the dialogue associated with the bot.
        chats (dict): A dictionary to store chat-related data.
        url (str): The URL for subscribing to chat updates.
    """

    def __init__(self, prefix, dialogue, session_token=None):
        self.prefix = prefix
        self.running = False
        self.token = None
        self.session_token = session_token
        self.user_id= None
        self.message_updater = None
        self.commands = {}
        self.events = {}
        self.dialogue = None
        self.chats = {}
        self.dialogue = dialogue
        self.url = f"https://ps.pndsn.com/v2/subscribe/sub-c-24884386-3cf2-11e5-8d55-0619f8945a4f/{self.dialogue}/0?heartbeat=300&tt=16925582152759863&tr=42&uuid=0P3kmjSyFv&pnsdk=PubNub-JS-Web%2F4.37.0"

    def start(self, token, selfbot=False):
        if token:
            # Create an event loop to run the async function
            loop = asyncio.get_event_loop()
            login = loop.run_until_complete(self.login_async(token))
            try:
                main_username = login[2]
            except:
                print("Invalid Session Token")
                exit()
            self.message_updater = MessageUpdater(self.url, main_username, selfbot=False)
            self.message_updater.callback = self.on_message
            self.user_id = login[3]
            self.token = token
            loop.run_until_complete(self.message_updater.run(selfbot))
            self.run_events()


    async def login_async(self,token):
        """:meta private:"""
        url = "https://mobile-elb.antich.at/functions/v2:profile.me?version=web/chat/2.0&localization=en"
        
        headers = CaseInsensitiveDict()
        headers["Host"] = "mobile-elb.antich.at"
        headers["Accept"] = "*/*"
        headers["Accept-Encoding"] = "gzip, deflate, br, zstd"
        headers["Accept-Language"] = "en-US,en;q=0.9"
        headers["Content-Length"] = "2"
        headers["Content-Type"] = "text/plain"
        headers["Origin"] = "https://www.antiland.com"
        headers["Priority"] = "u=1, i"
        headers["Referer"] = "https://www.antiland.com/"
        headers["Sec-Ch-Ua-Mobile"] = "?0"
        headers["Sec-Fetch-Dest"] = "empty"
        headers["Sec-Fetch-Mode"] = "cors"
        headers["Sec-Fetch-Site"] = "cross-site"
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 OPR/111.0.0.0"
        headers["X-Parse-Application-Id"] = "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5"
        headers["X-Parse-Session-Token"] = token
        data = {}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers,json=data) as response:
                if response.status == 200:
                    user_data = await response.json()
                    username = user_data.get("profileName", "N/A")
                    user_id = user_data.get("id", "N/A")
                    print(username)
                    gender = user_data.get("female", "N/A")
                    if gender:
                        emoji = "🚺"
                    else:
                        emoji = "🚹"
                    main_name = f"{username} {emoji}"
                    print(f"Logged in as {username}")
                    return (username, gender, main_name,user_id)
    
    async def on_message(self, sender, text):
        """
        Process incoming messages and execute commands.
        
        Args:
            sender (str): The sender of the message.
            text (str): The text of the message.
        """
        # Trigger message event
        for event_name, event_func in self.events.items():
            await event_func(text)

    def event(self, func):
        """
        Decorator to define custom event functions.

        Args:
            func (function): The event function to be registered.

        Returns:
            function: The decorated event function.
        """
        self.events[func.__name__] = func
        return func

    def run_events(self):
        """
        Run all registered event functions.
        """
        for event_name, event_func in self.events.items():
            asyncio.create_task(event_func())

    async def update_profile(self, session_token, **kwargs):
        """
        Update the bot's profile with the provided attributes.

        Args:
            session_token (str): The session token for authentication.
            kwargs: Keyword arguments for profile attributes (e.g., age, profileName, aboutMe).
        """
        base_url = f'https://mobile-elb.antich.at/classes/_User/{self.user_id}'
        common_data = {
            "_method": "PUT",
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": session_token
        }

        payload = common_data.copy()
        payload.update(kwargs)

        try:
            async with aiohttp.ClientSession() as session:
                async with session.put(base_url, json=payload) as response:
                    if response.status == 200:
                        print("Profile update successful.")
                    else:
                        print(f"Profile update failed with status code {response.status}.")
                        print(await response.text())
        except Exception as e:
            print(f"Error: {e}")

    async def get_stats(self, session_token):
        """
        Get account statistics.

        Args:
            session_token (str): The session token for authentication.

        Returns:
            Account: An Account instance containing account statistics.
        """
        url = "https://mobile-elb.antich.at/users/me"
        json_data = {
            "_method": "GET",
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "76b2aae2-0087-83e5-b86a-1a6d8ab69618",
            "_SessionToken": session_token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_data) as response:
                    if response.status == 200:
                        user_data = await response.json()
                        account = Account(user_data)
                        return account
                    else:
                        return None
        except Exception as e:
            print(f"Error: {e}")

    async def translate(self, token, message, message_id):
        """
        Translate a message.

        Args:
            token (str): The authentication token for the bot.
            message (str): The message to be translated.
            message_id (str): The message ID.

        Returns:
            str: The translated message.
        """
        url = "https://mobile-elb.antich.at/functions/translateMessage"
        json_data = {
            "text": message,
            "messageId": message_id,
            "persist": True,
            "lang": "en",
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "76b2aae2-0087-83e5-b86a-1a6d8ab69618",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_data) as translate:
                    translated = await translate.json()
                    result = translated.get("result")
                    return result
        except Exception as e:
            print(f"Error: {e}")

    async def get_contacts(self, token):
        """
        Get the bot's contacts.

        Args:
            token (str): The authentication token for the bot.

        Returns:
            list: A list of User instances representing bot contacts.
        """
        url = "https://mobile-elb.antich.at/functions/getContacts"
        json_payload = {
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    data = await r.json()
                    users = [User(user_data) for user_data in data["result"]]
                    return users
        except Exception as e:
            print(f"Error: {e}")

    async def add_contact(self, uuid, token):
        try:
            """
            Add a contact to the bot's contact list.

            Args:
                uuid (str): The UUID of the contact to be added.
                token (str): The authentication token for the bot.
            Returns:
                User: A User instance representing the specified user.
            """
            url = "https://www.antichat.me/uat/parse/functions/addContact"
            json_payload = {
                "contact": uuid,
                "v": 10001,
                "_ApplicationId": "VxfAeNw8Vuw2XKCN",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "23b9f34b-a753-e248-b7c2-c80e38bc3b40",
                "_SessionToken": token
            }

            try:
                async with aiohttp.ClientSession() as session:
                    async with session.post(url, json=json_payload) as r:
                        pass
            except Exception as e:
                print(f"Error: {e}")
        except Exception as e:
                print(f"Error: {e}")

    async def delete_contact(self, uuid, token):
        """
        Delete a contact from the bot's contact list.

        Args:
            uuid (str): The UUID of the contact to be deleted.
            token (str): The authentication token for the bot.
        """
        url = "https://mobile-elb.antich.at/functions/deleteContact"
        json_payload = {
            "contact": uuid,
            "v": 10001,
            "_ApplicationId": "VxfAeNw8Vuw2XKCN",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "23b9f34b-a753-e248-b7c2-c80e38bc3b40",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    pass
        except Exception as e:
            print(f"Error: {e}")

    async def block_user(self, uuid, token):
        """
        Block a user.

        Args:
            uuid (str): The UUID of the user to be blocked.
            token (str): The authentication token for the bot.
        """
        url = "https://mobile-elb.antich.at/functions/BlockPrivate"
        json_payload = {
            "blockedId": uuid,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    pass
        except Exception as e:
            print(f"Error: {e}")

    async def unblock_user(self, uuid, token):
        """
        Unblock a user.

        Args:
            uuid (str): The UUID of the user to be unblocked.
            token (str): The authentication token for the bot.
        """
        url = "https://mobile-elb.antich.at/functions/UnblockPrivate"
        json_payload = {
            "blockedId": uuid,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    pass
        except Exception as e:
            print(f"Error: {e}")

    async def get_dialogue(self, dialogue, token):
        """
        Get information about a specific dialogue.

        Args:
            dialogue (str): The ID of the dialogue to retrieve information for.
            token (str): The authentication token for the bot.

        Returns:
            Dialogue: A Dialogue instance representing the specified dialogue.
        """
        url = "https://mobile-elb.antich.at/functions/getDialogue"
        json_payload = {
            "dialogueId": dialogue,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    data = await r.json()
                    dialogue = Dialogue(data["result"])
                    return dialogue
        except Exception as e:
            print(f"Error: {e}")
    
    async def get_topchats(self, token):
        """
        Get the top chat dialogues.

        Args:
            token (str): The authentication token for the bot.

        Returns:
            list: A list of Dialogue instances representing the top chat dialogues.
        """
        url = "https://mobile-elb.antich.at/functions/getTopChats"
        json_payload = {
            "laterThen": {
              "iso": "2021-01-31T22:55:08.931Z",
              "__type": "Date"
            },
            "searchText": "",
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    data = await r.json()
                    dialogues = [Dialogue(dialogue) for dialogue in data["result"]]
                    return dialogues
        except Exception as e:
            print(f"Error: {e}")

    async def join_chat(self, token, dialogue):
        """
        Join a chat dialogue.

        Args:
            token (str): The authentication token for the bot.
            dialogue (str): The ID of the chat dialogue to join.
        """
        url = "https://mobile-elb.antich.at/functions/joinGroupChat"
        json_payload = {
            "chat": dialogue,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    data = await r.json()
        except Exception as e:
            print(f"Error: {e}")

    async def exit_chat(self, token, dialogue):
        """
        Exit a chat dialogue.

        Args:
            token (str): The authentication token for the bot.
            dialogue (str): The ID of the chat dialogue to exit.
        """
        url = "https://mobile-elb.antich.at/functions/exitGroupChat"
        json_payload = {
            "chat": dialogue,
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }

        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    data = await r.json()
        except Exception as e:
            print(f"Error: {e}")
    
    async def send_gift(self,gift_type,reciever,dialogue,session_token):
        """
        Send a gift

        Parameters:
        gift_type (str): The type of gift to send e.g. rose.
        reciever (str): The recipient's ID or username.
        dialogue (str): The ID of the dialogue or conversation related to the gift.
        session_token (str): A session token for authentication and authorization.

        Example:
        result = await bot.send_gift("rose", "user123", "dialogue456", "your_session_token_here")
        print(result)
        """
        url="https://mobile-elb.antich.at/functions/purchaseGift"
        json_payload={
                "currency": "karma",
                "artifactName": gift_type,
                "receiverId": reciever,
                "dialogueId": dialogue,
                "v": 10001,
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
                "_SessionToken": session_token
            }
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(url, json=json_payload) as r:
                    data = await r.json()
        except Exception as e:
            print(f"Error: {e}")
