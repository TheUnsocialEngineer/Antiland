class Account:
    """
    Represents an account on the Antiland platform, providing access to various account-related properties.

    Attributes:
        objectId (str): The unique identifier for the account.
        lastOpen (str): The timestamp of the last account activity.
        userLangs (list): A list of languages preferred by the user.
        username (str): The username associated with the account.
        country (str): The user's country.
        lang (str): The user's preferred language.
        avatar (str): The URL of the user's avatar.
        likesMale (bool): Indicates whether the user likes males.
        likesFemale (bool): Indicates whether the user likes females.
        color (str): The user's chosen color.
        antiKarma (int): The user's anti-karma value.
        rating (int): The user's rating on the platform.
        msgCount (int): The total count of messages sent by the user.
        pvtcCount (int): The total count of private chats the user has participated in.
        age (int): The user's age.
        search (str): The user's search preferences.
        createdAt (str): The timestamp when the account was created.
        updatedAt (str): The timestamp when the account was last updated.
        quest (str): The user's quest information.
        profileName (str): The user's profile name.
        pvtChannelId (str): The private channel ID.
        dOk (bool): Indicates whether the user has enabled D-OK.
        blockedBy (list): A list of users who have blocked the account.
        totalBans (int): The total count of bans applied to the user.
        more (str): Additional user information.
        female (bool): Indicates the user's gender (female or not).
        minKarma (int): The minimum required karma value.
        acceptRandoms (bool): Indicates whether the user accepts random connections.
        lastChangeDate (str): The timestamp of the last change to the user's account.
        email (str): The user's email address.
        emailIsVerified (bool): Indicates whether the user's email address is verified.
        artifacts (list): A list of user artifacts.
        lastAction (str): The timestamp of the user's last action.
        authData (str): User authentication data.
        emailIsValid (bool): Indicates whether the user's email is valid.
        ACL (str): The Access Control List associated with the account.
        __type (str): The type of the account data.
        className (str): The class name of the account data.
        sessionToken (str): The session token associated with the account.

    """ 
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
