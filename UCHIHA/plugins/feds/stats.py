from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_db import fed_bans, fed_chats


@app.on_message(filters.command("fedstats") & filters.group)
async def fedstats(_, m):
    fed = await fed_chats.find_one({"chat_id": m.chat.id})
    if not fed:
        return await m.reply("❌ No federation")

    fed_id = fed["fed_id"]
    bans = await fed_bans.find_one({"fed_id": fed_id}) or {}

    total_bans = len(bans) - 1 if bans else 0
    total_chats = await fed_chats.count_documents({"fed_id": fed_id})

    await m.reply(
        f"🏛 **Federation Stats**\n\n"
        f"• Fed: `{fed_id}`\n"
        f"• Banned users: `{total_bans}`\n"
        f"• Connected chats: `{total_chats}`"
    )
