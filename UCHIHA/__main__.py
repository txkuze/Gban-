import asyncio
import importlib

from pyrogram import idle

import config
from UCHIHA import LOGGER, app, userbot
from UCHIHA.core.call import PARTH
from UCHIHA.misc import sudo
from UCHIHA.plugins import ALL_MODULES
from UCHIHA.utils.database import get_banned_users, get_gbanned
from UCHIHA.plugins.tools.clone import restart_bots
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error(
            "✦🧾STRING SESSION IS EMPTY DO FILL THEM SIR IN CONFIG.PY🧾✦"
        )

    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("UCHIHA.plugins" + all_module)
    LOGGER("UCHIHA.plugins").info(" ✦FEATURES ASSISTED WITH GBAN CONTROLLER🧾 ✦")
    await userbot.start()
    await PARTH.start()
    await PARTH.decorators()
    LOGGER("UCHIHA").info("\n ✦🧾 MADE BY PARTH 🧾✦ \n")
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("UCHIHA").info("\n ✦🧾 MADE BY PARTH 🧾✦ \n")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
