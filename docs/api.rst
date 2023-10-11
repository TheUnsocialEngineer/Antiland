API Documentation
====================

This section provides documentation for various classes in the Antiland package.

Bot Class
---------

The `Bot` class represents a bot in the Antiland platform.

    Args:
        prefix (str): The command prefix to trigger bot commands.
        dialogue (str): The ID of the dialogue associated with the bot.
        session_token (str, optional): The session token for authentication. Defaults to None.

    Attributes:
        prefix (str): The command prefix to trigger bot commands.
        running (bool): A flag to indicate if the bot is running.
        token (str): The authentication token.
        session_token (str): The session token for authentication.
        message_updater (MessageUpdater): An instance of the MessageUpdater class.
        commands (dict): A dictionary to store bot commands.
        dialogue (str): The ID of the dialogue associated with the bot.
        chats (dict): A dictionary to store chat-related data.
        url (str): The URL for subscribing to chat updates.

    Methods:
        process_message(message, token): Process incoming messages and execute commands.
        start(token, selfbot=False): Start the bot, log in, and initiate message updates.
        login(token): Log in to the Antiland platform.
        command(name): Decorator to define bot commands.
        update_profile(session_token, **kwargs): Update the bot's profile.
        stats(session_token): Get account statistics.
        translate(token, message, message_id): Translate a message.
        get_contacts(token): Get the bot's contacts.
        add_contact(uuid, token): Add a contact to the bot's list.
        delete_contact(uuid, token): Delete a contact from the bot's list.
        block_user(uuid, token): Block a user.
        unblock_user(uuid, token): Unblock a user.
        get_dialogue(dialogue, token): Get information about a specific dialogue.
        get_topchats(token): Get the top chat dialogues.
        join_chat(token, dialogue): Join a chat dialogue.
        exit_chat(token, dialogue): Exit a chat dialogue.