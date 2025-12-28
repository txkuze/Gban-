from time import time
from UCHIHA.utils.superban_logger import superban_log


start = time()

await gban_user(user_id, reason)

end = time()

await superban_log(
    user=target_user,
    reason=reason,
    executor=m.from_user,
    total_bots=len(ALL_BOTS),
    total_chats=affected_chats,
    is_gban=True,
    is_fedban=True,
    time_taken=f"{int(end-start)} seconds",
)
