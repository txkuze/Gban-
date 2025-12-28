from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.errors import ChatAdminRequired, UserAdminInvalid

from UCHIHA import app
from UCHIHA.utils.mongo import is_gbanned


@app.on_message(filters.group & filters.incoming)
async def global_gban_watcher(_, message):
    if not message.from_user:
        return

    user_id = message.from_user.id

    if await is_gbanned(user_id):
        try:
            await message.chat.ban_member(user_id)
        except (ChatAdminRequired, UserAdminInvalid):
            pass
        except Exception:
            pass
