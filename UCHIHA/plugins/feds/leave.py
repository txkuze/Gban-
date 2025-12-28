from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_db import fed_chats


@app.on_message(filters.command("leavefed") & filters.group)
async def leavefed(_, m):
    await fed_chats.delete_one({"chat_id": m.chat.id})
    await m.reply("🚪 Group removed from federation")
