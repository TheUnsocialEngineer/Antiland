import aiohttp
from Antiland.message_updater import MessageUpdater
from Antiland.dialogue import Dialogue
from Antiland.account import Account
from Antiland.user import User
from Antiland.bot import Bot as botto
import asyncio
from requests.structures import CaseInsensitiveDict

class Bot:
    r"""
    The `Bot` class represents a bot on the Antiland platform, providing a variety of features and methods for interacting with the platform. 

    Args:
        prefix (str): The command prefix to trigger bot commands.
        dialogue (str): The ID of the dialogue associated with the bot.
        session_token (str, optional): The session token for authentication. Defaults to None.

    Attributes:
        prefix (str): The command prefix to trigger bot commands.
        running (bool): A flag to indicate if the bot is currently running.
        token (str): The authentication token.
        session_token (str): The session token for authentication.
        message_updater (MessageUpdater): An instance of the MessageUpdater class for managing incoming messages.
        commands (dict): A dictionary to store user-defined bot commands.
        events (dict): A dictionary to store user-defined event handlers.
        dialogue (str): The ID of the dialogue associated with the bot.
        chats (dict): A dictionary to store chat-related data.
        url (str): The URL for subscribing to chat updates.

    Methods:
        process_message(message, token): Process incoming messages and execute commands.
        start(token, selfbot=False): Start the bot, log in, and initiate message updates.
        login(token): Log in to the Antiland platform and retrieve user information.
        command(name): Decorator to define bot commands.
        update_profile(session_token, **kwargs): Update the bot's profile with specified attributes.
        get_stats(session_token): Retrieve account statistics.
        translate(token, message, message_id): Translate a message.
        get_contacts(token): Get the bot's contacts as instances of the User class.
        add_contact(uuid, token): Add a contact to the bot's contact list.
        delete_contact(uuid, token): Delete a contact from the bot's contact list.
        block_user(uuid, token): Block a user.
        unblock_user(uuid, token): Unblock a user.
        get_dialogue(dialogue, token): Retrieve information about a specific dialogue.
        get_topchats(token): Retrieve the top chat dialogues.
        join_chat(token, dialogue): Join a chat dialogue.
        exit_chat(token, dialogue): Exit a chat dialogue.

    Examples:
        bot = Bot(prefix='!', dialogue='4fkzGJsDs2', session_token='r:68ff2243463ee75afb4218f0a584b543')
        bot.start('your_auth_token')  # Start the bot with your authentication token.

    Usage:
        - Create a `Bot` instance by providing a command prefix, optional dialogue ID,session token.
        - Define bot commands using the `@bot.command` decorator and event handlers using the `@bot.event` decorator.
        - Start the bot with your authentication token using the `start` method.
        - The bot processes incoming messages, executes commands, and triggers event handlers based on message content.
        - Use various methods to interact with the Antiland platform, manage contacts, and perform actions within chat dialogues.

    Note:
        This class provides a framework for building and running an Antiland bot. You can extend its functionality by defining custom commands and event handlers.
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
        print(headers)
        data = {}
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers,json=data) as response:
                if response.status == 200:
                    user_data = await response.json()
                    username = user_data.get("result", {}).get("profileName", "N/A")
                    user_id = user_data.get("result", {}).get("id", "N/A")
                    print(username)
                    gender = user_data.get("result", {}).get("female", "N/A")
                    if gender:
                        emoji = "🚺"
                    else:
                        emoji = "🚹"
                    main_name = f"{username} {emoji}"
                    print(f"Logged in as {username}")
                    return (username, gender, main_name,user_id)

    def command(self, func):
        self.commands[func.__name__] = func
        return func

    async def on_message(self, message):
        if str(message.text).startswith(self.prefix):
            parts = str(message.text)[len(self.prefix):].split(" ")
            if len(parts) >= 1:  # Check if there is at least one part (the command itself)
                command = parts[0]
                if len(parts) >= 2:  # Check if there is a parameter
                    param = parts[1]
                else:
                    param = None  # No parameter provided
                if command in self.commands:
                    if param is not None:
                        await self.commands[command](param)
                    else:
                        await self.commands[command]()
        # Trigger message event
        for event_name, event_func in self.events.items():
            await event_func(message)

    def event(self, func):
        self.events[func.__name__] = func
        return func

    def run_events(self):
        for event_name, event_func in self.events.items():
            asyncio.create_task(event_func())

    async def update_profile(self, session_token, **kwargs):
        """
        Update the bot's profile with the provided attributes.

        Args:
            session_token (str): The session token for authentication.
            kwargs: Keyword arguments for profile attributes (e.g., age, profileName, aboutMe).
        """
        return(await botto.update_profile(self,session_token,**kwargs))

    async def get_stats(self, session_token):
        """
        Get account statistics.

        Args:
            session_token (str): The session token for authentication.

        Returns:
            Account: An Account instance containing account statistics.
        """
        return(await botto.get_stats(self,session_token))

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
        return(await botto.translate(self,token,message,message_id))

    async def get_contacts(self, token):
        """
        Get the bot's contacts.

        Args:
            token (str): The authentication token for the bot.

        Returns:
            list: A list of User instances representing bot contacts.
        """
        return(await botto.get_contacts(self,token))

    async def add_contact(self, uuid, token):
        """
        Add a contact to the bot's contact list.

        Args:
            uuid (str): The UUID of the contact to be added.
            token (str): The authentication token for the bot.
        Returns:
            User: A User instance representing the specified user.
        """
        return(await botto.add_contact(self,uuid,token))

    async def delete_contact(self, uuid, token):
        """
        Delete a contact from the bot's contact list.

        Args:
            uuid (str): The UUID of the contact to be deleted.
            token (str): The authentication token for the bot.
        """
        return(await botto.delete_contact(self,uuid,token))

    async def block_user(self, uuid, token):
        """
        Block a user.

        Args:
            uuid (str): The UUID of the user to be blocked.
            token (str): The authentication token for the bot.
        """
        return(await botto.block_user(self,uuid,token))

    async def unblock_user(self, uuid, token):
        """
        Unblock a user.

        Args:
            uuid (str): The UUID of the user to be unblocked.
            token (str): The authentication token for the bot.
        """
        return(await botto.unblock_user(self,uuid,token))

    async def get_dialogue(self, dialogue, token):
        """
        Get information about a specific dialogue.

        Args:
            dialogue (str): The ID of the dialogue to retrieve information for.
            token (str): The authentication token for the bot.

        Returns:
            Dialogue: A Dialogue instance representing the specified dialogue.
        """
        return(await botto.get_dialogue(self,dialogue,token))
    
    async def get_topchats(self, token):
        """
        Get the top chat dialogues.

        Args:
            token (str): The authentication token for the bot.

        Returns:
            list: A list of Dialogue instances representing the top chat dialogues.
        """
        return(await botto.get_topchats(self,token))

    async def join_chat(self, token, dialogue):
        """
        Join a chat dialogue.

        Args:
            token (str): The authentication token for the bot.
            dialogue (str): The ID of the chat dialogue to join.
        """
        return(await botto.join_chat(self,token,dialogue))

    async def exit_chat(self, token, dialogue):
        """
        Exit a chat dialogue.

        Args:
            token (str): The authentication token for the bot.
            dialogue (str): The ID of the chat dialogue to exit.
        """
        return(await botto.exit_chat(self,token,dialogue))
    
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
        return(await botto.send_gift(self,gift_type,reciever,dialogue,session_token))