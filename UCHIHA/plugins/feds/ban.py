from time import time
from UCHIHA.utils.superban_logger import superban_log
from UCHIHA.utils.feds_db import fed_chats


start = time()

await fedban_user(fed, user_id, reason)

chats_count = await fed_chats.count_documents({"fed_id": fed})
end = time()

await superban_log(
    user=m.reply_to_message.from_user,
    reason=reason,
    executor=m.from_user,
    fed_name=fed,
    total_bots=1,  # change if multi-bot stats
    total_chats=chats_count,
    is_gban=False,
    is_fedban=True,
    time_taken=f"{int(end-start)} seconds",
)
