import telebot
import settings
from telebot import types
import send
from loge import log_inf, log_err, log_deb

bot = telebot.TeleBot(settings.TOKEN)

cance_text = "Відмінити"
markup_cance = types.ReplyKeyboardMarkup()
cance_button = types.KeyboardButton(cance_text)
markup_cance = markup_cance.row(cance_button)

del_markup = types.ReplyKeyboardRemove()


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, ти можеш відправити валентинку тут. Введи текст відкритки",
                     reply_markup=markup_cance)
    bot.register_next_step_handler(message, get_user_text)


def get_user_text(message):
    if message.text != cance_text:
        user_text = message.text
        bot.send_message(message.chat.id, "Тепер напиши юзернейм кому відправити (@username без @)",
                         reply_markup=markup_cance)
        bot.register_next_step_handler(message, get_user_for, user_text)
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано")


def get_user_for(message, user_text):
    if message.text != cance_text:
        user_for = message.text
        bot.send_message(message.chat.id, "Тепер підпишись якось (можна як завгодно)",
                         reply_markup=markup_cance)
        bot.register_next_step_handler(message, get_user_from, user_text, user_for)
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано")


def get_user_from(message, user_text, user_for):
    if message.text != cance_text:
        user_from = message.text
        log_deb(f"username: {message.from_user.username}")
        log_deb(f"user_text: {user_text}")
        log_deb(f"user_for: {user_for}")
        log_deb(f"user_from: {user_from}")
        try:
            bot.send_message(message.chat.id, "Купідон побіг доставляти вашу валентинку, зачекайте декілька секунд)")
            send.sender(user_text=user_text, user_for=user_for, user_from=user_from, user_id = message.chat.id)
            bot.send_message(message.chat.id, "Валентинку доставлено")
            log_inf("SUCCES SEND")
        except Exception as ex:
            print(ex)
            log_err("ERROR SEND")
            bot.send_message(message.chat.id, "Вашу валентинку не вдалося доставити")
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано")


if __name__ == "__main__":
    bot.polling(none_stop=True)

