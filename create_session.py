from telethon import TelegramClient, events, sync
import settings
import sessions
from loge import log_inf

session_name = input("session name")

client = TelegramClient(session_name, settings.API_ID, settings.API_HASH)
client.start()
sessions.dop_session(session_name)
log_inf(f"success created session {session_name}")


