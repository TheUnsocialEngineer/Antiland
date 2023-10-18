import Antiland
import asyncio

session_token = ""
dialogue = ""
prefix = "!"

bot = Antiland.Bot(prefix, dialogue, session_token)

@bot.event
async def on_message(message):
    if str(message).startswith(prefix):
        print(f"command recieved {message}")


bot.start(session_token)