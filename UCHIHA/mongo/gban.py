from datetime import datetime
from typing import Optional, List

from UCHIHA.core.mongo import mongodb

# Collection
gbansdb = mongodb.gban


# ─────────────────────────────
# GETTERS
# ─────────────────────────────

async def is_gbanned(user_id: int) -> bool:
    return bool(await gbansdb.find_one({"user_id": user_id}))


async def get_gban(user_id: int) -> Optional[dict]:
    return await gbansdb.find_one({"user_id": user_id})


async def get_all_gbans() -> List[dict]:
    users = []
    async for user in gbansdb.find({"user_id": {"$gt": 0}}):
        users.append(user)
    return users


# ─────────────────────────────
# SETTERS
# ─────────────────────────────

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
