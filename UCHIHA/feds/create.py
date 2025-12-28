from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import create_fed, get_fed


@app.on_message(filters.command("newfed") & filters.private)
async def newfed(_, m):
    if len(m.command) < 2:
        return await m.reply("Usage: /newfed FED_NAME")

    fed_id = m.command[1]
    if await get_fed(fed_id):
        return await m.reply("❌ Federation already exists")

    await create_fed(fed_id, m.from_user.id)
    await m.reply(f"✅ Federation **{fed_id}** created")
