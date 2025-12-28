from typing import Dict, Union

from motor.motor_asyncio import AsyncIOMotorClient as MongoCli

from config import MONGO_DB_URI

mongo = MongoCli(MONGO_DB_URI)
db = mongo.UCHIHA

coupledb = db.couple


afkdb = db.afk

nightmodedb = db.nightmode

notesdb = db.notes

filtersdb = db.filters

gbansdb = db.gbans

async def _get_lovers(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["couple"]
    else:
        lovers = {}
    return lovers

async def _get_image(cid: int):
    lovers = await coupledb.find_one({"chat_id": cid})
    if lovers:
        lovers = lovers["img"]
    else:
        lovers = {}
    return lovers

async def get_couple(cid: int, date: str):
    lovers = await _get_lovers(cid)
    if date in lovers:
        return lovers[date]
    else:
        return False


async def save_couple(cid: int, date: str, couple: dict, img: str):
    lovers = await _get_lovers(cid)
    lovers[date] = couple
    await coupledb.update_one(
        {"chat_id": cid},
        {"$set": {"couple": lovers, "img": img}},
        upsert=True,


async def is_gbanned(user_id: int) -> bool:
    return bool(await gbansdb.find_one({"user_id": user_id}))


async def add_gban(
    user_id: int,
    username: str = None,
    reason: str = "No reason provided",
    banned_by: int = None,
):
    await gbansdb.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "user_id": user_id,
                "username": username,
                "reason": reason,
                "banned_by": banned_by,
                "date": datetime.utcnow(),
            }
        },
        upsert=True,
    )


    async def remove_gban(user_id: int):
    await gbansdb.delete_one({"user_id": user_id})
    )













from datetime import datetime
