from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import get_chat_fed, is_fed_admin
from UCHIHA.utils.feds_settings import set_silent


@app.on_message(filters.command("fedsilent") & filters.group)
async def fedsilent(_, m):
    fed = await get_chat_fed(m.chat.id)
    if not fed:
        return await m.reply("❌ No federation")

    if not await is_fed_admin(fed, m.from_user.id):
        return await m.reply("❌ Not fed admin")

    await set_silent(fed, True)
    await m.reply("🔕 Federation silent mode enabled")
