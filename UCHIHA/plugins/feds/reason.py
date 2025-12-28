from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import get_chat_fed
from UCHIHA.utils.feds_db import fed_bans


@app.on_message(filters.command("fedreason") & filters.group)
async def fedreason(_, m):
    if not m.reply_to_message:
        return await m.reply("Reply to user")

    fed = await get_chat_fed(m.chat.id)
    if not fed:
        return await m.reply("❌ No federation")

    data = await fed_bans.find_one({"fed_id": fed})
    if not data:
        return await m.reply("No record found")

    reason = data.get(str(m.reply_to_message.from_user.id))
    if not reason:
        return await m.reply("User not fedbanned")

    await m.reply(f"📄 **FedBan Reason:**\n{reason}")
