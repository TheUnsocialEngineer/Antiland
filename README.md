
## Usage/Examples

before you start you need to get the session token, dialogue id and chat url

to get the token and chat ID you use developer consoles network tab to look at any outgoing connection such as a sending a message, the session token is stored in the json payload e.g 

![App Screenshot](https://i.imgur.com/ZkVi80e.png)

to get the chat url you again use the network tab and this time you are looking for a heartbeat ping. once you find one you want to copy the request url as shown below

![App Screenshot](https://i.imgur.com/MaYCXdL.png)

below is a very basic example for logging in and registering a hello command
which when ran will send hello world into the chat

```python
import antiland

session_token="insert_session_token"
dialogue="insert_dialogue_id"
url="insert_chat_url"
prefix="!"

bot = anti.Bot(url,prefix,dialogue,session_token)

@bot.command("hello")
def say_hello():
    bot.send_message("hello world",session_token,dialogue)



if __name__ == "__main__":
    bot.start(session_token)
    
```

