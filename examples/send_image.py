import Antiland
from PIL import Image
import os

session_token="insert_session_token"
dialogue="insert_dialogue_id"
prefix="!"

bot = Antiland.Bot(prefix,dialogue,session_token)

@bot.command("image")
def image():
    print(os.getcwd())
    room = bot.get_dialogue(dialogue, session_token)
    
    image_path = "image_path"
    image = Image.open(image_path)

    # Save or display the resulting image
    output_path = "output.jpg"
    image.save(output_path)
    room.send_image(output_path, session_token, room.objectId)
    os.remove(output_path)

if __name__ == "__main__":
    bot.start(session_token)
    