from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import get_chat_fed


@app.on_message(filters.command("fedinfo") & filters.group)
async def fedinfo(_, m):
    fed = await get_chat_fed(m.chat.id)
    if not fed:
        return await m.reply("❌ No federation linked")

    await m.reply(f"🏛 Federation: **{fed}**")
