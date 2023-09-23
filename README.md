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

before you start you need to get the session token and a dialogue id

to get the token and chat ID you use developer consoles network tab to look at any outgoing connection such as a sending a message, the session token is stored in the json payload e.g 

![App Screenshot](https://i.imgur.com/ZkVi80e.png)


below is a very basic example for logging in and registering a hello command
which when ran will send hello world into the chat

```python
import Antiland

session_token="insert_session_token"
dialogue="insert_dialogue_id"
prefix="!"

bot = anti.Bot(prefix,dialogue,session_token)

@bot.command("hello")
def say_hello():
    room=bot.get_dialogue(dialogue,session_token)
    room.send_message("hello world",session_token,dialogue)



if __name__ == "__main__":
    bot.start(session_token)
    
```

