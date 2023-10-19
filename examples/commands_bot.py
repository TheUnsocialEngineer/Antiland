from Antiland.ext import commands
import asyncio

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