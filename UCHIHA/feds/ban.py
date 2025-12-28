from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import (
    get_chat_fed, is_fed_admin, fedban_user
)


@app.on_message(filters.command("fedban") & filters.group)
async def fedban(_, m):
    if not m.reply_to_message:
        return await m.reply("Reply to user")

    fed = await get_chat_fed(m.chat.id)
    if not fed:
        return await m.reply("❌ No federation linked")

    if not await is_fed_admin(fed, m.from_user.id):
        return await m.reply("❌ You are not a fed admin")

    reason = " ".join(m.command[1:]) or "No reason"
    user_id = m.reply_to_message.from_user.id

    await fedban_user(fed, user_id, reason)
    await m.reply("🚫 User **FedBanned** globally")
