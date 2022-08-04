import json
import settings
from loge import log_inf, log_deb


# mass = {"session_one" : []}


def save_json(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)
    log_deb("Використана команда збереження")


def load_json():
    with open('data.json', 'r') as fp:
        data = json.load(fp)
        log_deb("Використана команда завантаження")
        return data


def dop_session(session_name):
    mass = load_json()
    mass[f"{session_name}"] = []
    save_json(mass)
    log_inf(f"{session_name} додано до коллекції")


def use_session(user_id):
    mass = load_json()
    session = ""
    for a in mass:
        if user_id in mass[a]:
            session = a
            break
    if session == "":
        for b in mass:
            if len(mass[b]) < settings.AKK_LIMIT:
                mass[b].append(user_id)
                session = b
                save_json(mass)
                break
    log_deb(f"Використана сессія {session}")
    return session


def use_phone_session_one(phone_number):
    mass = load_json()
    session = ""
    add_phone = False
    for a in mass:
        if phone_number in mass[a]:
            session = a
            break
    if session == "":
        add_phone = True
        for b in mass:
            if len(mass[b]) < settings.AKK_LIMIT:
                session = b
                break
    log_deb(f"Використана перша фаза сессія для телефонів {session} з параметром {add_phone}")
    return [session, add_phone]


def use_phone_session_two(phone_number, session):
    mass = load_json()
    mass[session].append(phone_number)
    save_json(mass)
    log_deb("Викристана друга фаза сессії для телефонів")
