import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# 🔐 Bot & API credentials
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN")

# 👤 Owner & Bot Identity
OWNER_ID = int(getenv("OWNER_ID", "7905552682"))
OWNER_USERNAME = getenv("OWNER_USERNAME", "Swagger_Soul")
BOT_USERNAME = getenv("BOT_USERNAME", "AlexaxMusicRobot")
BOT_NAME = getenv("BOT_NAME", "Alexa Music")
ASSUSERNAME = getenv("ASSUSERNAME", "AlexaAssistant")

# 🗃️ Mongo & Logging
MONGO_DB_URI = getenv("MONGO_DB_URI")
LOGGER_ID = int(getenv("LOGGER_ID", "-1002226221442"))

# 🌐 Support & Repo
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/AarumiBots")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/AarumiChat")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/CARELESS-TG/Alexa_Music")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)

# 🔁 Heroku deployment
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

# ⏱️ Duration Limits
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "1800"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "1800"))
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "900"))

# 🎧 File size limits
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))

# 🔊 String Sessions (multi-assistant support)
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

# 🖼️ Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/b61227af05544deb76a34.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://telegra.ph/file/7bb907999ea7156227283.jpg")
PLAYLIST_IMG_URL = "https://telegra.ph/file/d723f4c80da157fca1678.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/4dc854f961cd3ce46899b.jpg"

# 🎵 Spotify (optional)
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

# 🔢 Playlist Fetch Limit
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

# 🔧 Utilities
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# 🧪 URL Validation
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - SUPPORT_CHANNEL must start with https://")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - SUPPORT_CHAT must start with https://")

# 👮 Filters & States
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
