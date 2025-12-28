from pyrogram import filters
from pyrogram.types import ChatMemberUpdated

from UCHIHA import app
from UCHIHA.utils.feds_funcs import get_chat_fed, is_fedbanned


@app.on_chat_member_updated(filters.group)
async def fed_join_ban(_, cm: ChatMemberUpdated):
    user = cm.new_chat_member.user
    if not user:
        return

    chat_id = cm.chat.id
    fed_id = await get_chat_fed(chat_id)

    if fed_id and await is_fedbanned(fed_id, user.id):
        try:
            await cm.chat.ban_member(user.id)
        except:
            pass
