.. currentmodule:: Antiland

.. _ext_commands_commands:

Commands
==========

One of the most appealing aspects of the command extension is how easy it is to define commands and
how you can arbitrarily nest groups and commands to have a rich sub-command system.

Commands are defined by attaching it to a regular Python function. The command is then invoked by the user using a similar
signature to the Python function.

.. warning::


For example, in the given command definition:

.. code-block:: python3

    @bot.command
    async def test():
        room=await bot.get_dialogue(dialogue)
        await room.send(f"test")

With the following prefix (``/``), it would be valled by the user via sending a message with the following content:

.. code-block:: none

    /test

Commands are registred using the :meth:`.Bot.command` decorator,as seen in the example above. 


Since the :meth:`.Bot.command` decorator is easier to understand and work with, it will be what we use throughout this documentation
documentation here.

Parameters
------------

Since we define commands by making Python functions, we can also pass paramaters to the command as arguments for 
advanced functionality

Certain parameter types do different things in the user side and most forms of parameter types are supported.

Positional
++++++++++++

The most basic form of a command with a passed paramater would be.
.. code-block:: python

    @bot.command
    async def test(arg):
        room=await bot.get_dialogue(dialogue)
        await room.send(f"test {arg}")

This is an example of a bot with two registered commands.
.. code-block:: python

    import Antiland
    import asyncio

    session_token = ""
    dialogue = ""
    prefix = "!"

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