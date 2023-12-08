# Antiland.py
## Make Antiland Chaotic Again


Antiland.py is a python package to turn any antiland user into a fully functioning
bot account similar to discord.py

![GitHub](https://img.shields.io/github/license/TheUnsocialEngineer/Anti.py) 
![PyPI - Version](https://img.shields.io/pypi/v/Antiland?labelColor=black&color=blue&link=https%3A%2F%2Fpypi.org%2Fproject%2FAntiland.py%2F)
![PyPI - Downloads](https://img.shields.io/pypi/dw/Antiland)






## Features

- Log in to an account
- send messages/images/videos 
- change profile settings
- Automate tedious tasks e.g banning/blocking
- It's python so go nuts



## Installation

Antiland requires Python3 to run.

to install run pip3 install Antiland

## Usage/Examples

before you start you need to get the session token which will allow you to log into the account and the dialogue id of the chat you want to listen for commands in

to get the token and you use developer consoles network tab to look at any outgoing connection such as a sending a message, the session token is stored in the json payload e.g 

![App Screenshot](https://i.imgur.com/ZkVi80e.png)


below is an example of a bot that prints every message it receives

```python
import Antiland
session_token = ""
dialogue = ""
prefix = "!"

bot = Antiland.Bot(prefix, dialogue, session_token)

@bot.event
async def on_message(message):
    # Implement your event handling logic here
    print(f"Received message from {message.sender_name}: {message.text}")

bot.start(session_token)
```


below is a very basic example for logging in and registering a hello command
which when ran will send hello world into the chat and register a debug command
which will send a message to the channel of your choice

```python
from Antiland.ext import commands

session_token = ""
dialogue = ""
prefix = "!"

bot = commands.Bot(prefix, dialogue, session_token)

@bot.command
async def say_hello():
    room = await bot.get_dialogue(dialogue, session_token)
    await room.send_message("hello world", session_token, dialogue)

@bot.command
async def debug():
    room =await bot.get_dialogue("enter dialogue id here", session_token)
    await room.send_message("BOT IS WORKING", session_token, dialogue)


bot.start(session_token)
    
```

for more examples read the [docs] (https://antiland.readthedocs.io/en/latest/)
