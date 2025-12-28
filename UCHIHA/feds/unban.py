from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import (
    get_chat_fed, is_fed_admin, unfedban_user
)


@app.on_message(filters.command("fedunban") & filters.group)
async def fedunban(_, m):
    if not m.reply_to_message:
        return await m.reply("Reply to user")

    fed = await get_chat_fed(m.chat.id)
    if not fed:
        return await m.reply("❌ No federation")

    if not await is_fed_admin(fed, m.from_user.id):
        return await m.reply("❌ You are not fed admin")

    await unfedban_user(fed, m.reply_to_message.from_user.id)
    await m.reply("✅ User **FedUnbanned**")
