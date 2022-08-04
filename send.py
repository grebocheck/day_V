from telethon import TelegramClient, events, sync
import settings
from asyncio import set_event_loop, new_event_loop
import sessions
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import InputPhoneContact
from telethon.tl.functions.contacts import ImportContactsRequest
from loge import log_err, log_deb


def get_user(username):
    with TelegramClient('bot2', settings.API_ID, settings.API_HASH) as client:
        user = client(GetFullUserRequest(username))
    return user


def sender(user_for, valentine, caption):
    set_event_loop(new_event_loop())
    num_session = sessions.use_session(get_user(user_for).user.id)
    if num_session != 0:
        with TelegramClient(num_session, settings.API_ID, settings.API_HASH) as client:
            client.start()
            client.send_message(user_for, "Привіт, вам валентинка 💌:")
            client.send_file(user_for, valentine, caption=caption)
            client.disconnect()
    else:
        log_err('ЗАКІНЧИЛИСЬ АККАУНТИ')
        raise Exception('ЗАКІНЧИЛИСЬ АККАУНТИ')


def sender_phone(user_phone, valentine, caption):
    try:
        sess_date = sessions.use_phone_session_one(phone_number=user_phone)
        set_event_loop(new_event_loop())
        num_session = sess_date[0]
        with TelegramClient(num_session, settings.API_ID, settings.API_HASH) as client:
            client.start()
            try:
                contact = InputPhoneContact(
                    client_id=0,
                    phone=user_phone,
                    first_name="FN",
                    last_name="LN"
                )
                client(ImportContactsRequest([contact]))
                log_deb(f"Користувач {user_phone} був доданий до контактів")
            except Exception as ex:
                print(ex)
                log_deb(f"Користувач {user_phone} НЕ був доданий до контактів")
            entity = client.get_entity(user_phone)
            client.send_message(entity, "Привіт, вам валентинка 💌:")
            client.send_file(entity, valentine, caption=caption)
            client.disconnect()
            sessions.use_phone_session_two(phone_number=user_phone, session=sess_date[0])
    except:
        log_err('ЗАКІНЧИЛИСЬ АККАУНТИ')
        raise Exception('ВИНИКЛА ПОМИЛКА')

# sender("heridium","valentines/0KNiqAHnKgWc.jpg")
# sender_phone("+19283253198", "valentines/0KNiqAHnKgWc.jpg",caption="ss")
