from telethon import TelegramClient, events, sync
import settings
from asyncio import set_event_loop, new_event_loop
import sessions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest


def get_user(username):
    with TelegramClient('bot1', settings.API_ID, settings.API_HASH) as client:
        user = client(GetFullUserRequest(username))
    return user


def sender(user_for, valentine, caption):
    set_event_loop(new_event_loop())
    num_session = sessions.use_session(get_user(user_for).user.id)
    if num_session != 0:
        client = TelegramClient(num_session, settings.API_ID, settings.API_HASH)
        client.start()
        client.send_file(user_for, valentine, caption=caption)
        client.disconnect()
    else:
        raise Exception('ЗАКІНЧИЛИСЬ АККАУНТИ')


def sender_phone(user_phone, valentine, caption):
    try:
        sess_date = sessions.use_phone_session_one(phone_number=user_phone)
        set_event_loop(new_event_loop())
        num_session = sess_date[0]
        client = TelegramClient(num_session, settings.API_ID, settings.API_HASH)
        client.start()
        try:
            contact = InputPhoneContact(
                client_id=0,
                phone=user_phone,
                first_name="FN",
                last_name="LN"
            )
            client(ImportContactsRequest([contact]))
            sessions.use_phone_session_two(phone_number=user_phone, session=sess_date[0])
        except Exception as ex:
            print(ex)
        entity = client.get_entity(user_phone)
        client.send_file(entity, valentine, caption=caption)
        client.disconnect()
    except:
        raise Exception('ВИНИКЛА ПОМИЛКА')

# sender("heridium","valentines/0KNiqAHnKgWc.jpg")
# sender_phone("+19283253198", "valentines/0KNiqAHnKgWc.jpg",caption="ss")
