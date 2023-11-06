class Account:
    def __init__(self, data):
        self._data = data
        

    @property
    def objectId(self):
        """The unique identifier for the account."""
        return self._data.get("objectId")

    @property
    def lastOpen(self):
        """The timestamp of the last account activity."""
        return self._data.get("lastOpen")

    @property
    def userLangs(self):
        """A list of languages preferred by the user."""
        return self._data.get("userLangs")

    @property
    def username(self):
        """The username associated with the account."""
        return self._data.get("username")

    @property
    def country(self):
        """The user's country."""
        return self._data.get("country")

    @property
    def lang(self):
        """The user's preferred language."""
        return self._data.get("lang")

    @property
    def avatar(self):
        """The URL of the user's avatar."""
        return self._data.get("avatar")

    @property
    def likesMale(self):
        """Indicates whether the user likes males."""
        return self._data.get("likesMale")

    @property
    def likesFemale(self):
        """Indicates whether the user likes females."""
        return self._data.get("likesFemale")

    @property
    def color(self):
        """The user's chosen color."""
        return self._data.get("color")

    @property
    def antiKarma(self):
        """The user's anti-karma value."""
        return self._data.get("antiKarma")

    @property
    def rating(self):
        """The user's rating on the platform."""
        return self._data.get("rating")

    @property
    def msgCount(self):
        """The total count of messages sent by the user."""
        return self._data.get("msgCount")

    @property
    def pvtcCount(self):
        """The total count of private chats the user has participated in."""
        return self._data.get("pvtcCount")

    @property
    def age(self):
        """The user's age."""
        return self._data.get("age")

    @property
    def search(self):
        """The user's search preferences."""
        return self._data.get("search")

    @property
    def createdAt(self):
        """The timestamp when the account was created."""
        return self._data.get("createdAt")

    @property
    def updatedAt(self):
        """The timestamp when the account was last updated."""
        return self._data.get("updatedAt")

    @property
    def quest(self):
        """The user's quest information."""
        return self._data.get("quest")

    @property
    def profileName(self):
        """The user's profile name."""
        return self._data.get("profileName")

    @property
    def pvtChannelId(self):
        """The private channel ID."""
        return self._data.get("pvtChannelId")

    @property
    def dOk(self):
        """Indicates whether the user has enabled D-OK."""
        return self._data.get("dOk")

    @property
    def blockedBy(self):
        """A list of users who have blocked the account."""
        return self._data.get("blockedBy")

    @property
    def totalBans(self):
        """The total count of bans applied to the user."""
        return self._data.get("totalBans")

    @property
    def more(self):
        """Additional user information."""
        return self._data.get("more")

    @property
    def female(self):
        """Indicates the user's gender (female or not)."""
        return self._data.get("female")

    @property
    def minKarma(self):
        """The minimum required karma value."""
        return self._data.get("minKarma")

    @property
    def acceptRandoms(self):
        """Indicates whether the user accepts random connections."""
        return self._data.get("acceptRandoms")

    @property
    def lastChangeDate(self):
        """The timestamp of the last change to the user's account."""
        return self._data.get("lastChangeDate")

    @property
    def email(self):
        """The user's email address."""
        return self._data.get("email")

    @property
    def emailIsVerified(self):
        """Indicates whether the user's email address is verified."""
        return self._data.get("emailIsVerified")

    @property
    def artifacts(self):
        """A list of user artifacts."""
        return self._data.get("artifacts")

    @property
    def lastAction(self):
        """The timestamp of the user's last action."""
        return self._data.get("lastAction")

    @property
    def authData(self):
        """User authentication data."""
        return self._data.get("authData")

    @property
    def emailIsValid(self):
        """Indicates whether the user's email is valid."""
        return self._data.get("emailIsValid")

    @property
    def ACL(self):
        """The Access Control List associated with the account."""
        return self._data.get("ACL")

    @property
    def __type(self):
        """The type of the account data."""
        return self._data.get("__type")

    @property
    def className(self):
        """The class name of the account data."""
        return self._data.get("className")

    
    