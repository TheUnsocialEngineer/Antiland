:orphan:

.. _quickstart:

.. currentmodule:: Antiland

Quickstart
===============

This page gives a brief introduction to the library. It assumes you have the library installed,
if you don't check the :ref:`installing` portion.

A Basic Antiland Bot
--------------------

Let's make a simple bot with 2 registered commands that send messages into the chat.

It looks something like this:

.. code-block:: python

    import Antiland
    import asyncio

    session_token = "" # insert session token here
    dialogue = ""   #enter chatid here
    prefix = "!" # prefix can be anything you want

    bot = Antiland.Bot(prefix, dialogue, session_token)

    @bot.command
    async def say_hello():
        room = await bot.get_dialogue(dialogue, session_token)
        await room.send_message("hello world", session_token, dialogue)

    @bot.command
    async def debug():
        room =await bot.get_dialogue("enter dialogue id here", session_token)
        await room.send_message("BOT IS WORKING", session_token, dialogue)
        
    bot.start(session_token)

Let's name this file ``antiland_bot_example.py``. Make sure not to name it ``antiland.py`` as that'll conflict
with the library.

If this is your first time using the library this can be quite overwhelming so lets go
step below.

1. The first line just imports the library, if this raises a :exc:`ModuleNotFoundError` or :exc:`ImportError`
   then head on over to :ref:`installing` section to make sure the library has been installed correctly
2. We then use the :meth:`Bot.command` decorator to register a command.
3. Finally, we run the bot with our session token.


Now that we've made a bot, we have to *run* the bot. Since we are using python we can run the bot 
using one of the commands below.

On Windows:

.. code-block:: shell

    $ py -3 example_bot.py

On other systems:

.. code-block:: shell

    $ python3 example_bot.py

Now you can try playing around with your basic bot.