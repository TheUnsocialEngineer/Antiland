import Antiland

session_token="insert_session_token"
dialogue="insert_dialogue_id"
prefix="!"

bot = Antiland.Bot(prefix,dialogue,session_token)

@bot.command("hello")
def say_hello():
    room=bot.get_dialogue(dialogue,session_token)
    room.send_message("hello world",session_token,dialogue)

@bot.command("debug")
def debug():
    room=bot.get_dialogue("enter dialogue id here",session_token)
    room.send_message("BOT IS WORKING",session_token,dialogue)

if __name__ == "__main__":
    bot.start(session_token)
    