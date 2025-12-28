# =====================================
# BASIC BOT CONFIG
# =====================================

API_ID = int(os.getenv("API_ID", "34999060"))
API_HASH = os.getenv("API_HASH", "8a4b8206da5f273c4147a091a9e9c73f")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Optional (for multi-assistant userbots)
SESSION_ONE = os.getenv("SESSION_ONE", None)
SESSION_TWO = os.getenv("SESSION_TWO", None)
SESSION_THREE = os.getenv("SESSION_THREE", None)
SESSION_FOUR = os.getenv("SESSION_FOUR", None)
SESSION_FIVE = os.getenv("SESSION_FIVE", None)

# =====================================
# DATABASE (MONGO)
# =====================================

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://knight4563:knight4563@cluster0.a5br0se.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME", "UCHIHA")

# =====================================
# OWNER / SUDO
# =====================================

OWNER_ID = int(os.getenv("OWNER_ID", "7852340648"))

# Space separated IDs
SUDO_USERS = list(
    map(int, os.getenv("SUDO_USERS", "7852340648").split())
) if os.getenv("SUDO_USERS") else []

# =====================================
# LOGGING / SUPERBANS
# =====================================

# Channel where gban / fedban / VC logs go
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID", "-1003132769250"))

# SUPERBAN logger GIF
SUPERBAN_GIF = os.getenv(
    "SUPERBAN_GIF",
    "https://files.catbox.moe/7osvoi.mp4"
)

# Auto pin superban logs
PIN_LOGS = bool(int(os.getenv("PIN_LOGS", 1)))

# =====================================
# FEDERATION SYSTEM
# =====================================

# Enable federation globally
ENABLE_FEDERATION = True

# Auto-gban on fedban
FED_TO_GBAN = True

# =====================================
# VC WATCHER
# =====================================

# Enable VC join watcher
ENABLE_VC_WATCHER = True

# Ban gbanned users when they join VC
VC_GBAN_ENFORCE = True

# =====================================
# MUSIC / STREAMING
# =====================================

DURATION_LIMIT = int(os.getenv("DURATION_LIMIT", 5400))  # seconds
PLAYLIST_LIMIT = int(os.getenv("PLAYLIST_LIMIT", 50))

# Images
STREAM_IMG_URL = os.getenv(
    "STREAM_IMG_URL",
    "https://files.catbox.moe/ddeho3.jpg"
)
SOUNCLOUD_IMG_URL = os.getenv(
    "SOUNCLOUD_IMG_URL",
    "https://telegra.ph/file/soundcloud.jpg"
)

TELEGRAM_VIDEO_URL = os.getenv(
    "TELEGRAM_VIDEO_URL",
    "https://files.catbox.moe/7osvoi.mp4"
)

# =====================================
# INLINE / CALLBACK SECURITY
# =====================================

# Banned users filter placeholder (filled at runtime)
BANNED_USERS = set()

# =====================================
# SUPPORT / LINKS
# =====================================

SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/snowy_hometown")
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/dark_musictm")

# =====================================
# MISC
# =====================================

TZ = os.getenv("TZ", "Asia/Kolkata")
LANGUAGE = os.getenv("LANGUAGE", "en")

# =====================================
# END
# =====================================
