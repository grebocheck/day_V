import json
from loge import log_inf, log_err, log_deb


# mass_sessions = {1:0}


def save_json(data):
    with open('data.json', 'w') as fp:
        json.dump(data, fp)


def load_json():
    with open('data.json', 'r') as fp:
        data = json.load(fp)
        return data


def use_session(num_session):
    mass = load_json()
    try:
        if mass[num_session] <= 50:
            mass[num_session] = mass[num_session] + 1
            save_json(mass)
            print(f"USED SESSION {num_session} : {mass[num_session]}")
    except Exception as e:
        print("ERROR: ")
        print(e)


def dop_session(session_name):
    mass = load_json()
    mass[f"{session_name}"] = 0
    save_json(mass)
    print(f"{session_name} додано до коллекції")


def get_session():
    mass = load_json()
    num_session = 0
    for a in mass:
        if mass[a] < 50:
            num_session = a
            break
    if num_session != 0:
        print(f"Обрано {num_session}")
        return num_session
    else:
        log_err("Закінчились аккаунти!")
        return num_session