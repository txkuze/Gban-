from datetime import datetime
from UCHIHA import app
from config import LOG_CHANNEL_ID


async def superban_log(
    user,
    reason: str,
    executor,
    fed_name: str = None,
    total_bots: int = 0,
    total_chats: int = 0,
    is_gban: bool = False,
    is_fedban: bool = False,
    time_taken: str = "N/A",
):
    now = datetime.now().strftime("%Y/%m/%d %I:%M %p")

    text = (
        f"#Is_SuperBan\n\n"
        f"USER : {user.mention}\n"
        f"USER ID : `{user.id}`\n\n"
        f"REASON : {reason}\n\n"
        f"FBAN EXECUTED : `{total_chats}`\n"
        f"GBANNED CHATS BOT : `{total_bots}`\n\n"
        f"REQUEST APPROVED BY : {executor.mention}\n"
        f"SUPERBAN REQUEST BY : {executor.mention}\n\n"
        f"TIME TAKEN FOR SUPERBAN : `{time_taken}`\n"
        f"DATE & TIME : `{now}`\n\n"
        f"IS GBANNED : `{is_gban}`\n"
        f"IS SUPER BANNED : `{is_fedban}`\n\n"
        f"UNBAN HERE : @YourUnbanBot\n"
        f"POWERED BY : @YourBotsNetwork"
    )

    try:
        await app.send_message(
            LOG_CHANNEL_ID,
            text,
            disable_web_page_preview=True,
        )
    except:
        pass
