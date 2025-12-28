from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import link_chat


@app.on_message(filters.command("joinfed") & filters.group)
async def joinfed(_, m):
    if len(m.command) < 2:
        return await m.reply("Usage: /joinfed FED_NAME")

    await link_chat(m.command[1], m.chat.id)
    await m.reply("✅ Group linked to federation")
