import requests
import base64
import requests
import json
import requests
import base64
import requests
import threading
from num2words import num2words
from datetime import datetime
import inflect

class MessageUpdater(threading.Thread):
    previous_message_text = None

    
    def __init__(self, url, username,callback):
        super().__init__()
        self.url = url
        self.username=username
        self.callback = callback
        self.running = False

    def run(self):
        
        def extract_message_text(json_response):
            messages = json_response.get("m", [])
            if messages:
                last_message = messages[-1]
                message_text = last_message.get("d", {}).get("message")
                return message_text
            return None

        def extract_message_sender(json_response):
            messages = json_response.get("m", [])
            if messages:
                last_message = messages[-1]
                message_sender=last_message.get("d", {}).get("sendersName")
                return message_sender
            return None
        
        self.running = True
        previous_message_text = None
        
        while self.running:
            response = requests.get(self.url)
            if response.status_code == 200:
                json_response = response.json()
                message_text = extract_message_text(json_response)
                message_sender = extract_message_sender(json_response)
                message_content = f"{message_sender}: {message_text}"
                if message_text and message_text != previous_message_text and message_sender == self.username:
                    previous_message_text = message_text
                    self.callback(message_text,message_sender)
                    
    def stop(self):
        self.running = False
    
class Message:
    def __init__(self, data):
        self.id = data["objectId"]
        self.text = data["message"]
        self.sender_id = data["senderId"]
        self.dialogue_id = data["dialogue"]

class User:
    def __init__(self, data):
        self.created_at = data.get("createdAt")
        self.updated_at = data.get("updatedAt")
        self.profile_name = data.get("profileName")
        self.age = data.get("age")
        self.female = data.get("female")
        self.avatar = data.get("avatar")
        self.rating = data.get("rating")
        self.anti_karma = data.get("antiKarma")
        self.blocked_by = data.get("blockedBy")
        self.blessed = data.get("blessed")
        self.vip_exp_date = data.get("vipExpDate", {}).get("iso")
        self.is_admin = data.get("isAdmin")
        self.is_vip = data.get("isVIP")
        self.accessories = data.get("accessories")
        self.premium_avatar = data.get("premiumAvatar")
        self.min_karma = data.get("minKarma")
        self.show_online = data.get("showOnline")
        self.about_me = data.get("aboutMe")
        self.object_id = data.get("objectId")
    
class Bot():

    def __init__(self,prefix,dialogue, session_token=None):
        self.prefix = prefix
        self.running = False
        self.token = None
        self.session_token = session_token
        self.message_updater = None
        self.commands = {}
        self.dialogue=None
        self.chats = {}
        self.dialogue=dialogue
        self.url=f"https://ps.pndsn.com/v2/subscribe/sub-c-24884386-3cf2-11e5-8d55-0619f8945a4f/{self.dialogue}/0?heartbeat=300&tt=16925582152759863&tr=42&uuid=0P3kmjSyFv&pnsdk=PubNub-JS-Web%2F4.37.0"

    def process_message(self, message,token):
        if str(message).startswith(self.prefix):
            param=False
            command = message[len(self.prefix):].split(" ")[0]
            try:
                param =message[len(self.prefix):].split(" ")[1]
            except:
                pass
            if command in self.commands and param:
                self.commands[command](param)
            elif command in self.commands:
                self.commands[command]()
            
    def start(self,token):
        if token:
            login=self.login(token)
            main_username=login[2]
            self.message_updater = MessageUpdater(self.url, main_username, self.process_message)
            self.message_updater.start()

    def login(self, token):
        url="https://mobile-elb.antich.at/users/me"
        json_data={
        "_method": "GET",
        "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
        "_ClientVersion": "js1.11.1",
        "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
        "_SessionToken": token
        }
        response = requests.post(url, json=json_data)
        
        if response.status_code == 200:
            user_data = response.json()
            username = user_data.get("profileName", "N/A")
            gender=user_data.get("female", "N/A")
            if gender:
                emoji="🚺"
            else:
                emoji="🚹"
            main_name=f"{username} {emoji}"
            print("Logged in as {}".format(username))
            return(username,gender,main_name)
    
    def command(self, name):
        def decorator(func):
            self.commands[name] = func
            return func
        return decorator
    
    def send_message(self,message,token=None,dialogue=None):
        url="https://mobile-elb.antich.at/classes/Messages"

        json={
        "receiver": "group",
        "dialogue": dialogue,
        "message": f"{message}",
        "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
        "_ClientVersion": "js1.11.1",
        "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
        "_SessionToken": token
        }

        try:
            r=requests.post(url,json=json)
            
            if r.status_code == 201:
                pass
            else:
                print(f"Request for sending message failed with status code {r.status_code}.")
        except Exception as e:
            print(e)
            print(" ")

    def send_video(filepath, token, dialogue):
        # Convert backslashes to forward slashes in the file path
        filepath = filepath.replace("\\", "/")
        
        with open(filepath, 'rb') as image_file:
            data = base64.b64encode(image_file.read()).decode("utf-8")
        
        url = "https://mobile-elb.antich.at/files/upload.mp4"
        url2 = "https://mobile-elb.antich.at/classes/Messages"
        
        json_payload = {
            "base64": data,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
            "_SessionToken": token
        }
        
        try:
            r = requests.post(url, json=json_payload)
            
            try:
                jsoner = json.loads(r.content.decode('utf-8'))
            except:
                jsoner = json.loads(r.content.decode('utf-8'))
            print(jsoner)
            url = jsoner["url"]
            name = jsoner["name"]
            json_payload2 = {
                "dialogue": dialogue,
                "message": "[video]",
                "photo": {
                    "name": name,
                    "url": url,
                    "__type": "File"
                },
                "receiver": "group",
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
                "_SessionToken": token
            }
            
            try:
                r = requests.post(url2, json=json_payload2)
                print(r.text)
            except Exception as e:
                print(f"error: {e}")
                print(" ")
        except Exception as e:
            print(f"error: {e}")
            print(" ")
    
    def send_image(self,filepath,token=None,dialogue=None):
        # Convert backslashes to forward slashes in the file path
        
        with open(filepath, 'rb') as image_file:
            data = base64.b64encode(image_file.read()).decode("utf-8")
        
        url = "https://mobile-elb.antich.at/files/upload.jpg"
        url2 = "https://mobile-elb.antich.at/classes/Messages"
        
        json_payload = {
            "base64": data,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
            "_SessionToken": token
        }
        
        try:
            r = requests.post(url, json=json_payload)
            
            try:
                jsoner = json.loads(r.content.decode('utf-8'))
            except:
                jsoner = json.loads(r.content.decode('utf-8'))
            
            url = jsoner["url"]
            name = jsoner["name"]
            
            json_payload2 = {
                "dialogue": dialogue,
                "message": "[photo]",
                "photo": {
                    "name": name,
                    "url": url,
                    "__type": "File"
                },
                "receiver": "group",
                "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
                "_ClientVersion": "js1.11.1",
                "_InstallationId": "d7559e27-cade-66a2-6ba9-4674e6d97864",
                "_SessionToken": token
            }
            
            r = requests.post(url2, json=json_payload2)
        except Exception as e:
            print(e)
            print(" ")
    
    def set_bio(token,bio):
        url = 'https://mobile-elb.antich.at/classes/_User/mV1UqOtkyL'

        data = {
            "female": False,
            "_method": "PUT",
            "aboutMe": bio,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "76b2aae2-0087-83e5-b86a-1a6d8ab69618",
            "_SessionToken": token
        }

        response = requests.put(url, json=data)

        if response.status_code == 200:
            pass
        else:
            print(f"Request for setting 'about me'failed with status code {response.status_code}.")
            print(response.text)
    
    def stats(self,session_token):
        url = "https://mobile-elb.antich.at/users/me"
        json_data = {
            "_method": "GET",
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "76b2aae2-0087-83e5-b86a-1a6d8ab69618",
            "_SessionToken": session_token
        }
        
        response = requests.post(url, json=json_data)
        
        if response.status_code == 200:
            user_data = response.json()

            def format_date(date_str):
                date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
                day = num2words(date_obj.day, to='ordinal')
                month = date_obj.strftime('%B')
                year = date_obj.year
                return f"{day}/{month}/{year}"

            # Extract and format the creation date
            created_iso = user_data.get("createdAt", "N/A")
            formatted_created = format_date(created_iso)

            # Other important user stats
            bans= user_data.get("totalBans", "N/A")
            p = inflect.engine()
            total_bans_text = p.number_to_words(bans)
            username = user_data.get("profileName", "N/A")
            rating = user_data.get("rating", "N/A")
            msg_count = user_data.get("msgCount", "N/A")
            pvtc_count = user_data.get("pvtcCount", "N/A")
            return(username,total_bans_text,rating,msg_count,pvtc_count)
    
    def translate(token,message,message_id):
        url="https://mobile-elb.antich.at/functions/translateMessage"
        json={
        "text": message,
        "messageId": message_id,
        "persist": True,
        "lang": "en",
        "v": 10001,
        "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
        "_ClientVersion": "js1.11.1",
        "_InstallationId": "76b2aae2-0087-83e5-b86a-1a6d8ab69618",
        "_SessionToken": token
        }
        translate=requests.post(url,json)
        translated=translate.json()
        result = translated.get("result")
        return(result)

    def get_contacts(self,token):
        url = "https://mobile-elb.antich.at/functions/getContacts"
        json_payload = {
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }
        r = requests.post(url, json=json_payload)
        data = r.json()
        users = [User(user_data) for user_data in data["result"]]
        return users
    
    def add_contact(self,uuid,token):
        url="https://www.antichat.me/uat/parse/functions/addContact"
        json_payload={
            "contact": uuid,
            "v": 10001,
            "_ApplicationId": "VxfAeNw8Vuw2XKCN",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "23b9f34b-a753-e248-b7c2-c80e38bc3b40",
            "_SessionToken": token
          }
        r=requests.post(url,json_payload)

    def get_messages(self,chatid, token):
        url = "https://mobile-elb.antich.at/functions/getMessagesAndRemoves"
        json_payload = {
            "dialogueId": chatid,
            "laterThan": {
                "iso": "2023-09-05T05:33:54.792Z",
                "__type": "Date"
            },
            "v": 10001,
            "_ApplicationId": "fUEmHsDqbr9v73s4JBx0CwANjDJjoMcDFlrGqgY5",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "3e355bb2-ce1f-0876-2e6b-e3b19adc4cef",
            "_SessionToken": token
        }
        r = requests.post(url, json=json_payload)
        data = r.json()
        messages_data = data["result"]["messages"]
        messages = [Message(message_data) for message_data in messages_data]
        return messages

    def like_message(self,messageid,senderid,token,dialogue):
        url="https://www.antichat.me/uat/parse/functions/loveMessage"
        json_payload={
            "messageId": messageid,
            "dialogueId": dialogue,
            "senderId": senderid,
            "v": 10001,
            "_ApplicationId": "VxfAeNw8Vuw2XKCN",
            "_ClientVersion": "js1.11.1",
            "_InstallationId": "23b9f34b-a753-e248-b7c2-c80e38bc3b40",
            "_SessionToken": token
        }
        r=requests.post(url,json_payload)