from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_db import feds
from UCHIHA.utils.feds_funcs import is_fed_owner, get_chat_fed


@app.on_message(filters.command("fedtransfer") & filters.group)
async def fedtransfer(_, m):
    if not m.reply_to_message:
        return await m.reply("Reply to new owner")

    fed = await get_chat_fed(m.chat.id)
    if not await is_fed_owner(fed, m.from_user.id):
        return await m.reply("❌ Not fed owner")

    await feds.update_one(
        {"fed_id": fed},
        {"$addToSet": {"owners": m.reply_to_message.from_user.id}}
    )
    await m.reply("👑 Ownership granted")
