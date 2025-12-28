from pyrogram import filters
from UCHIHA import app
from UCHIHA.utils.feds_funcs import add_fed_admin, get_chat_fed


@app.on_message(filters.command("addfedadmin") & filters.group)
async def addadmin(_, m):
    if not m.reply_to_message:
        return await m.reply("Reply to a user")

    fed = await get_chat_fed(m.chat.id)
    if not fed:
        return await m.reply("❌ This chat is not in a federation")

    await add_fed_admin(fed, m.reply_to_message.from_user.id)
    await m.reply("✅ User added as fed admin")
