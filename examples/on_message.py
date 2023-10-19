import Antiland
import asyncio

session_token = ""
dialogue = ""
prefix = "!"

bot = Antiland.Bot(prefix, dialogue, session_token)

@bot.event
async def on_message(message):
    # Implement your event handling logic here
    print(f"Received message from {message.sender_name}: {message.text}")
    if str(message.text).startswith(f"{prefix}moo"):
        room= await bot.get_dialogue(dialogue,session_token)
        await room.send_message("test",session_token,room.objectId)



bot.start(session_token)