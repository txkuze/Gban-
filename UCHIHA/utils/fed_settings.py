from .feds_db import fed_settings


async def set_fed_log(fed_id, chat_id):
    await fed_settings.update_one(
        {"fed_id": fed_id},
        {"$set": {"log_chat": chat_id}},
        upsert=True
    )


async def get_fed_log(fed_id):
    data = await fed_settings.find_one({"fed_id": fed_id})
    return data.get("log_chat") if data else None


async def set_silent(fed_id, status: bool):
    await fed_settings.update_one(
        {"fed_id": fed_id},
        {"$set": {"silent": status}},
        upsert=True
    )


async def is_silent(fed_id):
    data = await fed_settings.find_one({"fed_id": fed_id})
    return data.get("silent", False) if data else False
