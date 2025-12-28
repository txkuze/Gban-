from .feds_db import feds, fed_chats, fed_bans, fed_admins


# CREATE FED
async def create_fed(fed_id, owner):
    await feds.insert_one({
        "fed_id": fed_id,
        "owners": [owner]
    })
async def is_fed_owner(fed_id, user_id):
    fed = await feds.find_one({"fed_id": fed_id})
    return user_id in fed.get("owners", [])
    
# LINK CHAT
async def link_chat(fed_id: str, chat_id: int):
    await fed_chats.update_one(
        {"chat_id": chat_id},
        {"$set": {"fed_id": fed_id}},
        upsert=True
    )


# ADD FED ADMIN
async def add_fed_admin(fed_id: str, user_id: int):
    await fed_admins.update_one(
        {"fed_id": fed_id},
        {"$addToSet": {"admins": user_id}},
        upsert=True
    )


# FEDBAN USER
async def fedban_user(fed_id: str, user_id: int, reason: str = None):
    await fed_bans.update_one(
        {"fed_id": fed_id},
        {"$set": {str(user_id): reason or "No reason"}},
        upsert=True
    )


# CHECK FEDBAN
async def is_fedbanned(fed_id: str, user_id: int):
    data = await fed_bans.find_one({"fed_id": fed_id})
    if not data:
        return False
    return str(user_id) in data


# GET CHAT FED
async def get_chat_fed(chat_id: int):
    data = await fed_chats.find_one({"chat_id": chat_id})
    return data["fed_id"] if data else None
