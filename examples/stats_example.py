import Antiland
import asyncio

session_token="insert_session_token"
dialogue="insert_dialogue_id"
prefix="!"

bot = Antiland.Bot(prefix,dialogue,session_token)

@bot.command
async def stats():
    stats=bot.stats(session_token)
    # Create a message with the formatted stats
    message=(
        f"Karma: {stats.rating}\n"f"Messages: {stats.msgCount}\n"
        f"Private chats: {stats.pvtcCount}\n"
        f"Timеs Ive Been Yeeted: {stats.totalBans} times\n"
        f"Blocked by: {len(stats.blockedBy)}\n"
    )
    print(message)
    room= await bot.get_dialogue(dialogue,session_token)
    await room.send_message(message,session_token,room.objectId)


bot.start(session_token)