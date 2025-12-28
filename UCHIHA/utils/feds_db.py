from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_DB_URI

mongo = AsyncIOMotorClient(MONGO_DB_URI)
db = mongo.UCHIHA

feds = db.feds
fed_chats = db.fed_chats
fed_bans = db.fed_bans
fed_admins = db.fed_admins
fed_settings = db.fed_settings
fed_logs = db.fed_logs
