from datetime import datetime

class User:
    r"""
     The `user` class represents a User profile on the Antiland platform.

    Methods:
        get_time(self, date_str): Gets time from a datetime iso.
        get_date(self, date_str): Gets date from a datetime iso
        get_formatted_datetime(self, date_str): Essentially the same as get_time but extracts from a certain json structure for getting certain times
        get_formatted_date(self, date_str): Essentially the same as get_date but extracts from a certain json structure for getting certain dates
    """
    def __init__(self, data):
        self._data = data

    @property
    def created_at(self):
        r"""Users account creation date and time in iso format"""
        return self._data.get("createdAt")

    @property
    def updated_at(self):
        r""""Users account creation date and time in iso format"""
        return self._data.get("updatedAt")

    @property
    def profile_name(self):
        r"""Users profile name"""
        return self._data.get("profileName")

    @property
    def age(self):
        """Users age"""
        return self._data.get("age")

    @property
    def female(self):
        """Boolean for if user is female or not"""
        return self._data.get("female")

    @property
    def avatar(self):
        """Users avatar number"""
        return self._data.get("avatar")

    @property
    def rating(self):
        """Users Karma amount"""
        return self._data.get("rating")

    @property
    def anti_karma(self):
        """Users AntiKarma amount"""
        return self._data.get("antiKarma")

    @property
    def blocked_by(self):
        """List of UUIDS who have blocked the user"""
        return self._data.get("blockedBy")

    @property
    def blessed(self):
        """Boolean for if user is blessed or not"""
        return self._data.get("blessed")

    @property
    def vip_exp_date(self):
        r"""Users VIP expiration date and time in iso format"""
        return self._data.get("vipExpDate")

    @property
    def prison_exp_date(self):
        r"""Users prison expiration date and time in iso format"""
        return self._data.get("inPrisonTill")

    @property
    def is_admin(self):
        """Boolean for if user is Admin or not"""
        return self._data.get("isAdmin")

    @property
    def is_vip(self):
        """Boolean for if user is VIP or not"""
        return self._data.get("isVIP")

    @property
    def accessories(self):
        """List of the integer values of what Accessories the user has"""
        return self._data.get("accessories")

    @property
    def premium_avatar(self):
        """Users premium avatar number if applicable"""
        return self._data.get("premiumAvatar")

    @property
    def min_karma(self):
        """Minimum Karma required to message the user"""
        return self._data.get("minKarma")

    @property
    def show_online(self):
        """Boolean for if user shows as online or not"""
        return self._data.get("showOnline")
    
    @property
    def about_me(self):
        """Users About Me"""
        return self._data.get("aboutMe")

    @property
    def object_id(self):
        r"""Users UUID"""
        return self._data.get("objectId")

    @property
    def created_at_time(self):
        r"""Users account creation time formatted from created_at"""
        return self.get_time(self.created_at)

    @property
    def created_at_date(self):
        r"""Users account creation date formatted from created_at"""
        return self.get_date(self.created_at)

    @property
    def vip_exp_time(self):
        r"""Users VIP expiration time formatted from prison_exp_date"""
        return self.get_formatted_datetime(self.vip_exp_date)

    @property
    def vip_exp_date_date(self):
        r"""Users VIP expiration date formatted from prison_exp_date"""
        return self.get_formatted_date(self.vip_exp_date)

    @property
    def prison_exp_date_date(self):
        r"""Users prison expiration date formatted from prison_exp_date"""
        return self.get_formatted_date(self.prison_exp_date)

    @property
    def prison_exp_time(self):
        r"""Users prison expiration time formatted from prison_exp_date"""
        return self.get_formatted_datetime(self.prison_exp_date)

    def get_time(self, date_str):
        r""":meta private:"""
        if date_str:
            date_time = datetime.fromisoformat(date_str)
            return date_time.strftime("%H:%M:%S")
        else:
            return None

    def get_date(self, date_str):
        r""":meta private:"""
        if date_str:
            date_time = datetime.fromisoformat(date_str)
            return date_time.strftime("%d/%m/%y")
        else:
            return None

    def get_formatted_datetime(self, date_data):
        r""":meta private:"""
        if date_data and 'iso' in date_data:
            iso_date_str = date_data['iso']
            date_time = datetime.fromisoformat(iso_date_str)
            return date_time.strftime("%H:%M:%S")
        else:
            return None

    def get_formatted_date(self, date_data):
        r""":meta private:"""
        if date_data and 'iso' in date_data:
            iso_date_str = date_data['iso']
            date_time = datetime.fromisoformat(iso_date_str)
            return date_time.strftime('%d/%m/%Y')
        else:
            return None
 