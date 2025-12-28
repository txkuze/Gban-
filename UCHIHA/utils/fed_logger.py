from UCHIHA import app
from .feds_settings import get_fed_log


async def fed_log(fed_id, text):
    chat = await get_fed_log(fed_id)
    if chat:
        try:
            await app.send_message(chat, text)
        except:
            pass
