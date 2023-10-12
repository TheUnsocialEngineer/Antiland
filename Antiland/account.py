class Account:
    def __init__(self, data):
        self._data = data

    @property
    def objectId(self):
        return self._data.get("objectId")

    @property
    def lastOpen(self):
        return self._data.get("lastOpen")

    @property
    def userLangs(self):
        return self._data.get("userLangs")

    @property
    def username(self):
        return self._data.get("username")

    @property
    def country(self):
        return self._data.get("country")

    @property
    def lang(self):
        return self._data.get("lang")

    @property
    def avatar(self):
        return self._data.get("avatar")

    @property
    def likesMale(self):
        return self._data.get("likesMale")

    @property
    def likesFemale(self):
        return self._data.get("likesFemale")

    @property
    def color(self):
        return self._data.get("color")

    @property
    def antiKarma(self):
        return self._data.get("antiKarma")

    @property
    def rating(self):
        return self._data.get("rating")

    @property
    def msgCount(self):
        return self._data.get("msgCount")

    @property
    def pvtcCount(self):
        return self._data.get("pvtcCount")

    @property
    def age(self):
        return self._data.get("age")

    @property
    def search(self):
        return self._data.get("search")

    @property
    def createdAt(self):
        return self._data.get("createdAt")

    @property
    def updatedAt(self):
        return self._data.get("updatedAt")

    @property
    def quest(self):
        return self._data.get("quest")

    @property
    def profileName(self):
        return self._data.get("profileName")

    @property
    def pvtChannelId(self):
        return self._data.get("pvtChannelId")

    @property
    def dOk(self):
        return self._data.get("dOk")

    @property
    def blockedBy(self):
        return self._data.get("blockedBy")

    @property
    def totalBans(self):
        return self._data.get("totalBans")

    @property
    def more(self):
        return self._data.get("more")

    @property
    def female(self):
        return self._data.get("female")

    @property
    def minKarma(self):
        return self._data.get("minKarma")

    @property
    def acceptRandoms(self):
        return self._data.get("acceptRandoms")

    @property
    def lastChangeDate(self):
        return self._data.get("lastChangeDate")

    @property
    def email(self):
        return self._data.get("email")

    @property
    def emailIsVerified(self):
        return self._data.get("emailIsVerified")

    @property
    def artifacts(self):
        return self._data.get("artifacts")

    @property
    def lastAction(self):
        return self._data.get("lastAction")

    @property
    def authData(self):
        return self._data.get("authData")

    @property
    def emailIsValid(self):
        return self._data.get("emailIsValid")

    @property
    def ACL(self):
        return self._data.get("ACL")

    @property
    def __type(self):
        return self._data.get("__type")

    @property
    def className(self):
        return self._data.get("className")

    @property
    def sessionToken(self):
        return self._data.get("sessionToken")
