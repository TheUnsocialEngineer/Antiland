from datetime import datetime

class User:
    def __init__(self, data):
        self._data = data

    @property
    def created_at(self):
        return self._data.get("createdAt")

    @property
    def updated_at(self):
        return self._data.get("updatedAt")

    @property
    def profile_name(self):
        return self._data.get("profileName")

    @property
    def age(self):
        return self._data.get("age")

    @property
    def female(self):
        return self._data.get("female")

    @property
    def avatar(self):
        return self._data.get("avatar")

    @property
    def rating(self):
        return self._data.get("rating")

    @property
    def anti_karma(self):
        return self._data.get("antiKarma")

    @property
    def blocked_by(self):
        return self._data.get("blockedBy")

    @property
    def blessed(self):
        return self._data.get("blessed")

    @property
    def vip_exp_date(self):
        return self._data.get("vipExpDate")

    @property
    def prison_exp_date(self):
        return self._data.get("inPrisonTill")

    @property
    def is_admin(self):
        return self._data.get("isAdmin")

    @property
    def is_vip(self):
        return self._data.get("isVIP")

    @property
    def accessories(self):
        return self._data.get("accessories")

    @property
    def premium_avatar(self):
        return self._data.get("premiumAvatar")

    @property
    def min_karma(self):
        return self._data.get("minKarma")

    @property
    def show_online(self):
        return self._data.get("showOnline")

    @property
    def about_me(self):
        return self._data.get("aboutMe")

    @property
    def object_id(self):
        return self._data.get("objectId")