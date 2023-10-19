from Antiland.ext import commands
import requests

session_token = ""
dialogue = ""
prefix = "!"

bot = commands.Bot(prefix, dialogue, session_token)


@bot.command
async def joke():  # b'\xfc'
    room= await bot.get_dialogue(dialogue,session_token)
    headers = {
        "Accept": "application/json"
    }
   
    with requests.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = req.json()
    await room.send_message(r["joke"],session_token,room.objectId)