from pyrogram import filters
from pyrogram.errors import ChatAdminRequired

from UCHIHA import app
from UCHIHA.utils.feds_funcs import get_chat_fed, is_fedbanned


@app.on_message(filters.group & filters.incoming)
async def fed_auto_ban(_, message):
    if not message.from_user:
        return

    chat_id = message.chat.id
    user_id = message.from_user.id

    fed_id = await get_chat_fed(chat_id)
    if not fed_id:
        return

    if await is_fedbanned(fed_id, user_id):
        try:
            await message.chat.ban_member(user_id)
        except ChatAdminRequired:
            pass
            
async def fedwatch(_, m):
    if not m.from_user:
        return

    fed = await get_chat_fed(m.chat.id)
    if fed and await is_fedbanned(fed, m.from_user.id):
        try:
            await m.chat.ban_member(m.from_user.id)
        except:
            pass
