import telebot
import settings
from telebot import types
import send
from loge import log_inf, log_err, log_deb
import photos_4

log_inf("Ініціалізація бота")
bot = telebot.TeleBot(settings.TOKEN)

# Тексти бота
cance_text = "Відмінити ❌"

films_text = "Фільми 🎬"
gachi_text = "Гачі 🔥"
memes_text = "Меми 🌚"
nani_text = "Няшні 🥰"
theme_mass = {films_text: "films", gachi_text: "gachi", memes_text: "memes", nani_text: "nani"}

Yes_text = "Так ✅"
No_text = "Ні ❌"

continue_text = "Продовжити"

s_phone_text = "по номеру телефону ☎️"
s_username_text = "по @username ✨"
s_none_text = "не відправляти ❌"

ban_text = "Ви забанені в боті! ❌"

start_text = "Привіт, цей бот допоможе вам створити валентинку❤️, оберіть фон для валентинки"
cance_compleate_text = "Створення валентинки скасовано ❌, якщо хочете почати заново, натисніть /start"
incorect_theme = "Цієї теми немає в меню, будь ласка оберіть тему з меню 🥸"
get_num_text = "Чудово, обери фон для валентинки за її номером 💌"
incorect_num = "Фону за таким номером немає, будь ласка вкажіть існуючий номер картинки 🥸"
get_from_text = "Підпишіть СЕБЕ 🐰 як вам хочеться від третьої особи (наприклад: твого зайчика) до 30 символів"
get_for_text = "Підпишіть ОДЕРЖУВАЧА 🐰 як вам хочеться від третьої особи (наприклад: твого зайчика) до 30 символів"
incorect_text = "Будь ласка, введіть коректно текст"
get_caption_text = "За бажанням, можете ввести текстове повідомлення , як підпис до валентинки 💌 (до 2.000 символів)"
view_photo_text = "Ваша валентинка💌:"
get_send_ways = "Виберіть спосіб відправки📕"
compleate_text = """Валентинка успішно доставлена. 
Сподіваємося бот допоміг вам та вашій симпатії прикрасити цей день🥰

Якщо хочете відправити ще, натисність /start 😇"""
incorect_way = "Виберіть коректно спосіб відправки 🥸"
get_phone_text = "Введіть номер телефону отримувача (+380XXXXXXXXX) ☎️"
get_username_text = "Введіть @username отримувача ✨"
error_text = "Виникла помилка при відправці повідомлення цьому користувачу, спробуйте ввести ще раз 🥸"
go_send_text = "Біжу відправляти валентинку 🕊💌"

# Клавиатура відміни
markup_cance = types.ReplyKeyboardMarkup()
cance_button = types.KeyboardButton(cance_text)
markup_cance = markup_cance.row(cance_button)

# Пуста клавіатура для видалення попередньої
del_markup = types.ReplyKeyboardRemove()

# Клавіатура вибору шаблону 1-7
num_mass = ["1", "2", "3", "4", "5", "6", "7"]
num_markup = types.ReplyKeyboardMarkup()
num_markup = num_markup.row(types.KeyboardButton("1"),
                            types.KeyboardButton("2"),
                            types.KeyboardButton("3"))
num_markup = num_markup.row(types.KeyboardButton("4"),
                            types.KeyboardButton("5"),
                            types.KeyboardButton("6"))
num_markup = num_markup.row(types.KeyboardButton("7"),
                            cance_button)

# Клавіатура вибору теми
theme_markup = types.ReplyKeyboardMarkup()
films_button = types.KeyboardButton(films_text)
gachi_button = types.KeyboardButton(gachi_text)
memes_button = types.KeyboardButton(memes_text)
nani_button = types.KeyboardButton(nani_text)
theme_markup = theme_markup.row(films_button, gachi_button)
theme_markup = theme_markup.row(memes_button, nani_button)
theme_markup = theme_markup.row(cance_button)

# Клавіатура підтвердження
tf_markup = types.ReplyKeyboardMarkup()
tf_markup = tf_markup.row(types.KeyboardButton(Yes_text),
                          types.KeyboardButton(No_text))

# Клавіатура підпису під картинку
caption_markup = types.ReplyKeyboardMarkup()
caption_markup = caption_markup.row(types.KeyboardButton(continue_text),
                                    cance_button)

# Клавіатура вибору способу відправки
s_phone_button = types.KeyboardButton(s_phone_text)
s_username_button = types.KeyboardButton(s_username_text)
s_none_button = types.KeyboardButton(s_none_text)
way_markup = types.ReplyKeyboardMarkup()
way_markup = way_markup.row(s_phone_button).row(s_username_button).row(s_none_button)


# Стартова команда, пропонує користувачу вибрати тему валентинки
@bot.message_handler(commands=['start'])
def start(message):
    if settings.WHITE_LIST_BOOL:
        log_deb(f"Користувач {message.from_user.username} або ж {message.from_user.id} використав команду /start")
        if message.from_user.id in settings.WHITE_LIST:
            bot.send_message(message.chat.id, start_text,
                             reply_markup=theme_markup)
            bot.register_next_step_handler(message, get_theme)
        else:
            log_inf(
                f"Користувач {message.from_user.username} або ж {message.from_user.id} не отримав доступ так як забанений")
            bot.send_message(message.chat.id, ban_text, reply_markup=del_markup)
    else:
        log_deb(f"Користувач {message.from_user.username} або ж {message.from_user.id} використав команду /start")
        if message.from_user.id not in settings.BAN_LIST:
            bot.send_message(message.chat.id, start_text,
                             reply_markup=theme_markup)
            bot.register_next_step_handler(message, get_theme)
        else:
            log_inf(
                f"Користувач {message.from_user.username} або ж {message.from_user.id} не отримав доступ так як забанений")
            bot.send_message(message.chat.id, ban_text, reply_markup=del_markup)


# Вибір теми, пропонує вибрати номер шаблону которий цікавить
def get_theme(message):
    if message.text != cance_text:
        if message.text in theme_mass:
            theme = theme_mass[message.text]
            img = open(f"templates/menu/{theme}.png", 'rb')
            bot.send_photo(message.chat.id, photo=img, caption=get_num_text,
                           reply_markup=num_markup)
            bot.register_next_step_handler(message, get_num, theme)
        else:
            bot.send_message(message.chat.id, incorect_theme,
                             reply_markup=theme_markup)
            bot.register_next_step_handler(message, get_theme)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


# Вибір номеру картинки, пропонує написати від кого валентинка
def get_num(message, theme):
    if message.text != cance_text:
        if message.text in num_mass:
            number = message.text
            bot.send_message(message.chat.id, get_from_text,
                             reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_from_user, theme, number)
        else:
            bot.send_message(message.chat.id, incorect_num,
                             reply_markup=num_markup)
            bot.register_next_step_handler(message, get_num, theme)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


# Ввід від кого валентинка, пропонує написати кому валентинка
def get_from_user(message, theme, number):
    if message.text != cance_text:
        try:
            if len(message.text) != 0 and len(message.text) <= 30:
                from_user = message.text
                bot.send_message(message.chat.id, get_for_text,
                                 reply_markup=markup_cance)
                bot.register_next_step_handler(message, get_for_user, theme, number, from_user)
            else:
                bot.send_message(message.chat.id, incorect_text,
                                 reply_markup=markup_cance)
                bot.register_next_step_handler(message, get_from_user, theme, number)
        except:
            log_deb(f"{message.from_user.id} відправив щось замість тексту!")
            bot.send_message(message.chat.id, incorect_text,
                             reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_from_user, theme, number)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


# Ввід для кого валентинка, пропонує по бажанню ввести підпис під картинку
def get_for_user(message, theme, number, from_user):
    if message.text != cance_text:
        try:
            if len(message.text) != 0 and len(message.text) <= 30:
                for_user = message.text
                bot.send_message(message.chat.id, get_caption_text,
                                 reply_markup=caption_markup)
                bot.register_next_step_handler(message, get_caption, theme, number, from_user, for_user)
            else:
                bot.send_message(message.chat.id, incorect_text,
                                 reply_markup=markup_cance)
                bot.register_next_step_handler(message, get_for_user, theme, number, from_user)
        except:
            log_deb(f"{message.from_user.id} відправив щось замість тексту!")
            bot.send_message(message.chat.id, incorect_text,
                             reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_for_user, theme, number, from_user)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


# Ввід підпису під картинку, виводить сформовану валентинку
def get_caption(message, theme, number, from_user, for_user):
    if message.text != cance_text:
        try:
            if len(message.text) == 0 or message.text == continue_text or len(message.text) > 2000:
                caption = ""
            else:
                caption = message.text
            image = f"templates/{theme}/{number}.jpg"
            image_name = photos_4.get_image(image, for_user, from_user)
            bot.send_message(message.chat.id, view_photo_text)
            log_deb(f"{message.from_user.id} створив валентинку {image_name}")
            img = open(image_name, 'rb')
            bot.send_photo(message.chat.id, photo=img, caption=caption)
            bot.send_message(message.chat.id, get_send_ways, reply_markup=way_markup)
            bot.register_next_step_handler(message, get_way, image_name, caption)
        except:
            log_deb(f"{message.from_user.id} відправив щось замість тексту!")
            caption = message.text
            image = f"templates/{theme}/{number}.jpg"
            image_name = photos_4.get_image(image, for_user, from_user)
            bot.send_message(message.chat.id, view_photo_text)
            log_deb(f"{message.from_user.id} створив валентинку {image_name}")
            img = open(image_name, 'rb')
            bot.send_photo(message.chat.id, photo=img, caption=caption)
            bot.send_message(message.chat.id, get_send_ways, reply_markup=way_markup)
            bot.register_next_step_handler(message, get_way, image_name, caption)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


# Вибір способу відправки
def get_way(message, image_name, caption):
    if message.text != s_none_text:
        if message.text == s_phone_text:
            bot.send_message(message.chat.id, get_phone_text,
                             reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_phone_num, image_name, caption)
        elif message.text == s_username_text:
            bot.send_message(message.chat.id, get_username_text,
                             reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_username, image_name, caption)
        else:
            bot.send_message(message.chat.id, incorect_way, reply_markup=way_markup)
            bot.register_next_step_handler(message, get_way, image_name, caption)
    else:
        bot.send_message(message.chat.id, compleate_text, reply_markup=del_markup)


# При відправки по номеру телефону, введеня номеру телефону
def get_phone_num(message, image_name, caption):
    if message.text != cance_text:
        phone_num = message.text
        log_deb(f"{message.from_user.id} ввів номер {phone_num}")
        try:
            bot.send_message(message.chat.id, go_send_text)
            send.sender_phone(user_phone=phone_num, valentine=image_name, caption=caption)
            bot.send_message(message.chat.id, compleate_text, reply_markup=del_markup)
            log_deb(f"{phone_num} отримав валентинку")
        except Exception as ex:
            print(ex)
            log_err(f"{phone_num} не зміг отримати валентинку")
            bot.send_message(message.chat.id, error_text, reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_phone_num, image_name, caption)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


# При відправки по юзернейму, введення юзернейму
def get_username(message, image_name, caption):
    if message.text != cance_text:
        username = message.text
        log_deb(f"{message.from_user.id} ввів юзернейм {username}")
        try:
            bot.send_message(message.chat.id, go_send_text)
            send.sender(user_for=username, valentine=image_name, caption=caption)
            bot.send_message(message.chat.id, compleate_text, reply_markup=del_markup)
            log_deb(f"{username} отримав валентинку")
        except Exception as ex:
            print(ex)
            log_err(f"{username} не зміг отримати валентинку")
            bot.send_message(message.chat.id, error_text, reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_username, image_name, caption)
    else:
        bot.send_message(message.chat.id, cance_compleate_text, reply_markup=del_markup)


if __name__ == "__main__":
    while True:
        try:
            log_inf("Запуск бота")
            bot.polling(none_stop=True)
        except Exception as ex:
            log_err("МЕГА ФАТАЛЬНА ПОМИЛКА, БОТ УПАВ, БОТ УПАВ")
            print(ex)
