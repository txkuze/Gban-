from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import ChatMemberUpdated

from Uchiha import app
from UCHIHA.utils.mongo import is_gbanned
from config import LOG_CHANNEL_ID


@app.on_chat_member_updated(filters.group)
async def vc_join_logger(_, cm: ChatMemberUpdated):
    user = cm.new_chat_member.user
    chat = cm.chat

    if not user:
        return

    # Only trigger on VC join
    if cm.old_chat_member and cm.new_chat_member:
        if (
            cm.old_chat_member.is_in_video_chat
            and not cm.new_chat_member.is_in_video_chat
        ):
            return

        if (
            not cm.old_chat_member.is_in_video_chat
            and cm.new_chat_member.is_in_video_chat
        ):
            # USER JOINED VC
            action = "Iɢɴᴏʀᴇᴅ"

            if await is_gbanned(user.id):
                try:
                    await chat.ban_member(user.id)
                    action = "Gʙᴀɴɴᴇᴅ"
                except:
                    action = "Iɢɴᴏʀᴇᴅ"

            text = (
                "🧾 #JᴏɪɴVɪᴅᴇᴏCʜᴀᴛ\n"
                f"✦ Nᴀᴍᴇ :  {user.first_name}\n"
                f"✦ ɪᴅ : {user.id}\n"
                f"✦ Aᴄᴛɪᴏɴ : {action}"
            )

            try:
                await app.send_message(LOG_CHANNEL_ID, text)
            except:
                pass
