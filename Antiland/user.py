from datetime import datetime

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
        self.vip_exp_date = data.get("vipExpDate")
        self.prison_exp_date=data.get("inPrisonTill")
        self.is_admin = data.get("isAdmin")
        self.is_vip = data.get("isVIP")
        self.accessories = data.get("accessories")
        self.premium_avatar = data.get("premiumAvatar")
        self.min_karma = data.get("minKarma")
        self.show_online = data.get("showOnline")
        self.about_me = data.get("aboutMe") 
        self.object_id = data.get("objectId")

    @property
    def created_at_time(self):
         return self.created_at.split("T")[1].split(".")[0]

    @property
    def created_at_date(self):
         return self.created_at.split("T")[0]

    @property
    def vip_exp_time(self):
        if self.vip_exp_date and 'iso' in self.vip_exp_date:
            iso_date_str = self.vip_exp_date['iso']
            vip_datetime = datetime.fromisoformat(iso_date_str)
            return vip_datetime.strftime("%H:%M:%S")
        else:
            return None

    @property
    def vip_exp_date_date(self):
        if self.vip_exp_date and 'iso' in self.vip_exp_date:
            iso_date_str = self.vip_exp_date['iso']
            vip_datetime = datetime.fromisoformat(iso_date_str)
            return vip_datetime.strftime("%d:%m:%y")
        else:
            return None

    @property
    def prison_exp_date_date(self):
        if self.prison_exp_date and 'iso' in self.prison_exp_date:
            iso_date_str = self.prison_exp_date['iso']
            prison_datetime = datetime.fromisoformat(iso_date_str)
            return prison_datetime.strftime('%d/%m/%Y')
        else:
            return None

    @property
    def prison_exp_time(self):
        if self.prison_exp_date and 'iso' in self.prison_exp_date:
            iso_date_str = self.prison_exp_date['iso']
            prison_datetime = datetime.fromisoformat(iso_date_str)
            return prison_datetime.strftime('%H:%M:%S')
        else:
            return None