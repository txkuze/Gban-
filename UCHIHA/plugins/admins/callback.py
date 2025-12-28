import asyncio

from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from UCHIHA import YouTube, app
from UCHIHA.core.call import PARTH
from UCHIHA.misc import SUDOERS, db
from UCHIHA.utils.database import (
    get_active_chats,
    get_lang,
    get_upvote_count,
    is_active_chat,
    is_music_playing,
    is_nonadmin_chat,
    music_off,
    music_on,
    set_loop,
)
from UCHIHA.utils.decorators.language import languageCB
from UCHIHA.utils.formatters import seconds_to_min
from UCHIHA.utils.inline import (
    close_markup,
    stream_markup,
    stream_markup_timer,
    telegram_markup,
    telegram_markup_timer,
)
from UCHIHA.utils.stream.autoclear import auto_clean
from UCHIHA.utils.thumbnails import get_thumb
from config import (
    BANNED_USERS,
    SOUNCLOUD_IMG_URL,
    STREAM_IMG_URL,
    TELEGRAM_AUDIO_URL,
    TELEGRAM_VIDEO_URL,
    adminlist,
    confirmer,
    votemode,
)
from strings import get_string

checker = {}
upvoters = {}


@app.on_callback_query(filters.regex("ADMIN") & ~BANNED_USERS)
@languageCB
async def del_back_playlist(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    command, chat = callback_request.split("|")
    if "_" in str(chat):
        bet = chat.split("_")
        chat = bet[0]
        counter = bet[1]
    chat_id = int(chat)
    if not await is_active_chat(chat_id):
        return await CallbackQuery.answer(_["general_5"], show_alert=True)
    mention = CallbackQuery.from_user.mention

    if command == "UpVote":
        if chat_id not in votemode:
            votemode[chat_id] = {}
        if chat_id not in upvoters:
            upvoters[chat_id] = {}

        voters = (upvoters[chat_id]).get(CallbackQuery.message.id)
        if not voters:
            upvoters[chat_id][CallbackQuery.message.id] = []

        vote = (votemode[chat_id]).get(CallbackQuery.message.id)
        if not vote:
            votemode[chat_id][CallbackQuery.message.id] = 0

        if CallbackQuery.from_user.id in upvoters[chat_id][CallbackQuery.message.id]:
            upvoters[chat_id][CallbackQuery.message.id].remove(
                CallbackQuery.from_user.id
            )
            votemode[chat_id][CallbackQuery.message.id] -= 1
        else:
            upvoters[chat_id][CallbackQuery.message.id].append(
                CallbackQuery.from_user.id
            )
            votemode[chat_id][CallbackQuery.message.id] += 1

        upvote = await get_upvote_count(chat_id)
        get_upvotes = int(votemode[chat_id][CallbackQuery.message.id])

        if get_upvotes >= upvote:
            votemode[chat_id][CallbackQuery.message.id] = upvote
            try:
                exists = confirmer[chat_id][CallbackQuery.message.id]
                current = db[chat_id][0]
            except:
                return await CallbackQuery.edit_message_text("ғᴀɪʟᴇᴅ.")

            if current["vidid"] != exists["vidid"] or current["file"] != exists["file"]:
                return await CallbackQuery.edit_message_text(_["admin_35"])

            await CallbackQuery.edit_message_text(_["admin_37"].format(upvote))
            command = counter
            mention = "ᴜᴘᴠᴏᴛᴇs"
        else:
            upl = InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        text=f"👍 {get_upvotes}",
                        callback_data=f"ADMIN  UpVote|{chat_id}_{counter}",
                    )
                ]]
            )
            await CallbackQuery.answer(_["admin_40"], show_alert=True)
            return await CallbackQuery.edit_message_reply_markup(reply_markup=upl)

    else:
        is_non_admin = await is_nonadmin_chat(CallbackQuery.message.chat.id)
        if not is_non_admin and CallbackQuery.from_user.id not in SUDOERS:
            admins = adminlist.get(CallbackQuery.message.chat.id)
            if not admins or CallbackQuery.from_user.id not in admins:
                return await CallbackQuery.answer(_["admin_14"], show_alert=True)

    if command == "Pause":
        await music_off(chat_id)
        await PARTH.pause_stream(chat_id)
        await CallbackQuery.message.reply_text(_["admin_2"].format(mention))

    elif command == "Resume":
        await music_on(chat_id)
        await PARTH.resume_stream(chat_id)
        await CallbackQuery.message.reply_text(_["admin_4"].format(mention))

    elif command in ["Stop", "End"]:
        await PARTH.stop_stream(chat_id)
        await set_loop(chat_id, 0)
        await CallbackQuery.message.reply_text(_["admin_5"].format(mention))

    elif command in ["Skip", "Replay"]:
        check = db.get(chat_id)
        txt = f"➻ sᴛʀᴇᴀᴍ {'sᴋɪᴩᴩᴇᴅ' if command=='Skip' else 'ʀᴇ-ᴘʟᴀʏᴇᴅ'} 🎄\n│ \n└ʙʏ : {mention} 🥀"
        await PARTH.skip_stream(chat_id, check[0]["file"])
        await CallbackQuery.edit_message_text(txt, reply_markup=close_markup(_))


async def markup_timer():
    while not await asyncio.sleep(4):
        for chat_id in await get_active_chats():
            if not await is_music_playing(chat_id):
                continue
            playing = db.get(chat_id)
            if not playing:
                continue

            mystic = playing[0].get("mystic")
            markup = playing[0].get("markup")
            if not mystic:
                continue

            language = await get_lang(chat_id)
            _ = get_string(language)

            buttons = (
                stream_markup_timer(
                    _, playing[0]["vidid"], chat_id,
                    seconds_to_min(playing[0]["played"]),
                    playing[0]["dur"],
                )
                if markup == "stream"
                else telegram_markup_timer(
                    _, chat_id,
                    seconds_to_min(playing[0]["played"]),
                    playing[0]["dur"],
                )
            )

            try:
                await mystic.edit_reply_markup(
                    reply_markup=InlineKeyboardMarkup(buttons)
                )
            except:
                pass


asyncio.create_task(markup_timer())
