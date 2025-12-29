# =====================================
# LOAD ENV
# =====================================
import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# =====================================
# BASIC BOT CONFIG
# =====================================

API_ID = int(os.getenv("API_ID", "34999060"))
API_HASH = os.getenv("API_HASH", "8a4b8206da5f273c4147a091a9e9c73f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

BOT_NAME = os.getenv("BOT_NAME", "GBAN CONTROLLER")
BOT_USERNAME = os.getenv("BOT_USERNAME", "Gban_controllerbot")
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "owner_of_itachi")
ASSUSERNAME = os.getenv("ASSUSERNAME", "superban_assistant")

# =====================================
# ASSISTANT SESSIONS
# =====================================

STRING_SESSION = os.getenv("STRING_SESSION", "")
STRING_SESSION2 = os.getenv("STRING_SESSION2", None)
STRING_SESSION3 = os.getenv("STRING_SESSION3", None)
STRING_SESSION4 = os.getenv("STRING_SESSION4", None)
STRING_SESSION5 = os.getenv("STRING_SESSION5", None)
STRING_SESSION6 = os.getenv("STRING_SESSION6", None)
STRING_SESSION7 = os.getenv("STRING_SESSION7", None)

# =====================================
# DATABASE (MONGO)
# =====================================

MONGO_DB_URI = os.getenv(
    "MONGO_DB_URI",
    "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
)
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "UCHIHA")

# =====================================
# OWNER / SUDO
# =====================================

OWNER_ID = int(os.getenv("OWNER_ID", "7852340648"))

SUDO_USERS = list(
    map(int, os.getenv("SUDO_USERS", str(OWNER_ID)).split())
)

# =====================================
# LOGGING / FED / GBAN
# =====================================

LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-1003132769250"))
LOGGER_ID = int(os.getenv("LOGGER_ID", "-1003580678666"))

SUPERBAN_GIF = os.getenv(
    "SUPERBAN_GIF",
    "https://files.catbox.moe/7osvoi.mp4"
)

PIN_LOGS = bool(int(os.getenv("PIN_LOGS", 1)))

# =====================================
# FEDERATION SYSTEM
# =====================================

ENABLE_FEDERATION = True
FED_TO_GBAN = True

# =====================================
# VC WATCHER
# =====================================

ENABLE_VC_WATCHER = True
VC_GBAN_ENFORCE = True

# =====================================
# MUSIC / STREAMING
# =====================================

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 17000))
PLAYLIST_LIMIT = int(os.getenv("PLAYLIST_LIMIT", 50))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 5242880000))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 5242880000))

def time_to_seconds(time):
    return sum(int(x) * 60**i for i, x in enumerate(reversed(time.split(":"))))

DURATION_LIMIT = time_to_seconds(f"{DURATION_LIMIT_MIN}:00")

# =====================================
# SPOTIFY
# =====================================

SPOTIFY_CLIENT_ID = os.getenv(
    "SPOTIFY_CLIENT_ID",
    "1c21247d714244ddbb09925dac565aed"
)
SPOTIFY_CLIENT_SECRET = os.getenv(
    "SPOTIFY_CLIENT_SECRET",
    "709e1a2969664491b58200860623ef19"
)

# =====================================
# AUTO LEAVE / DOWNLOAD
# =====================================

AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(os.getenv("ASSISTANT_LEAVE_TIME", 9000))

SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", 9999999))
SONG_DOWNLOAD_DURATION_LIMIT = int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", 9999999))

# =====================================
# HEROKU / UPSTREAM
# =====================================

HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv(
    "UPSTREAM_REPO",
    "https://github.com/itzarjuna1/ANAYA-music"
)
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN")

# =====================================
# IMAGES
# =====================================

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
PLAYLIST_IMG_URL = os.getenv("PLAYLIST_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
STATS_IMG_URL = os.getenv("STATS_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")

STREAM_IMG_URL = os.getenv("STREAM_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
SOUNCLOUD_IMG_URL = os.getenv("SOUNCLOUD_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")

TELEGRAM_AUDIO_URL = os.getenv("TELEGRAM_AUDIO_URL", "https://files.catbox.moe/7osvoi.mp4")
TELEGRAM_VIDEO_URL = os.getenv("TELEGRAM_VIDEO_URL", "https://files.catbox.moe/7osvoi.mp4")

YOUTUBE_IMG_URL = os.getenv("YOUTUBE_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
SPOTIFY_ARTIST_IMG_URL = os.getenv("SPOTIFY_ARTIST_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
SPOTIFY_ALBUM_IMG_URL = os.getenv("SPOTIFY_ALBUM_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")
SPOTIFY_PLAYLIST_IMG_URL = os.getenv("SPOTIFY_PLAYLIST_IMG_URL", "https://files.catbox.moe/ddeho3.jpg")

# =====================================
# SUPPORT
# =====================================

SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/snowy_hometown")
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/dark_musictm")

if SUPPORT_CHAT and not re.match("(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("SUPPORT_CHAT must start with https://")

if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("SUPPORT_CHANNEL must start with https://")

# =====================================
# RUNTIME / FILTERS
# =====================================

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# =====================================
# MISC
# =====================================

TZ = os.getenv("TZ", "Asia/Kolkata")
LANGUAGE = os.getenv("LANGUAGE", "en")
