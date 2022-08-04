from telethon import TelegramClient, events, sync
import settings
from asyncio import set_event_loop, new_event_loop
import sessions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest

client = TelegramClient('bot1', settings.API_ID, settings.API_HASH)
client.start()

phone_number = "+380968793084"

contact = InputPhoneContact(
        client_id=0,
        phone=phone_number,
        first_name="FN",
        last_name="LN"
    ) # For new contacts you should use client_id = 0
result = client(ImportContactsRequest([contact]))
# print(contact)
# #client.send_message(result.users[0], 'Hello, friend!')

entity = client.get_entity(phone_number)
client.send_message(entity, 'Тест')

client.disconnect()
# sender("grebocheck","valentines/0KNiqAHnKgWc.jpg")