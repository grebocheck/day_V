import telebot
import settings
from telebot import types
import send
from loge import log_inf, log_err, log_deb
import photos_two
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot(settings.TOKEN)

cance_text = "Відмінити"
markup_cance = types.ReplyKeyboardMarkup()
cance_button = types.KeyboardButton(cance_text)
markup_cance = markup_cance.row(cance_button)

del_markup = types.ReplyKeyboardRemove()

num_markup = types.ReplyKeyboardMarkup()
num_markup = num_markup.row(types.KeyboardButton("1"),
                            types.KeyboardButton("2"),
                            types.KeyboardButton("3"))
num_markup = num_markup.row(types.KeyboardButton("4"),
                            types.KeyboardButton("5"),
                            types.KeyboardButton("6"))
num_markup = num_markup.row(types.KeyboardButton("7"),
                            types.KeyboardButton("8"),
                            types.KeyboardButton("9"))
num_markup = num_markup.row(types.KeyboardButton("10"),
                            cance_button)

Yes_text = "Так"
No_text = "Ні"
tf_markup = types.ReplyKeyboardMarkup()
tf_markup = tf_markup.row(types.KeyboardButton(Yes_text),
                          types.KeyboardButton(No_text))

albom = ["AgACAgIAAxkBAALtpmH6bd1vFVkN0OOgf3xZXKP0O_vmAAK3tjEbqIrYS_nqYfcUP_KCAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALtqGH6bd2cawbyuGG4FBF5l6P51M84AAK4tjEbqIrYS2dUK5ufYw_mAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALtqWH6bd03rl7yHNj67AXRmmVx5FSuAAK5tjEbqIrYS1HT2qwdsxagAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALtrGH6bd5cjuhfvIF4cFFy8d6YWf25AAK6tjEbqIrYS7bB_Yw4XxbYAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALtr2H6bd4NF86f4OEi-YaIv-zNDI1BAAK7tjEbqIrYSz2nD3RVgjzpAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALts2H6bd_9riSyHTx9al4BBk90L5FvAAK8tjEbqIrYS3NIpFBVWLtqAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALttWH6bd-AesaJB93zacMNqzOFYRPTAAK9tjEbqIrYSwZlD33Ec51FAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALtt2H6beAwJOxVmGFxX1eXWLAAAcw0KQACvrYxG6iK2EttsAgO47q1BwEAAwIAA3kAAyME",
         "AgACAgIAAxkBAALtvGH6beDQlF31k8j7b4HgJhng5QFaAAK_tjEbqIrYS91wJ_-0dK7SAQADAgADeQADIwQ",
         "AgACAgIAAxkBAALtvmH6beGKxJbKkBK-pFjHr5m7z8sGAALAtjEbqIrYS0SB0vkwlOyRAQADAgADeQADIwQ"]


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привіт, ти можеш відправити валентинку тут. Вибери шаблон валентинки",
                     reply_markup=num_markup)
    media_group = []
    for num in range(1, 11):
        media_group.append(InputMediaPhoto(open('photos/%d.png' % num, 'rb')))
    bot.send_media_group(message.chat.id, media=media_group)
    bot.register_next_step_handler(message, get_user_photo)


def get_user_photo(message):
    if message.text != cance_text:
        if message.text in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            user_photo = message.text
            print(user_photo)
            bot.send_message(message.chat.id, "Тепер напиши текст валентинки",
                             reply_markup=markup_cance)
            bot.register_next_step_handler(message, get_user_text, user_photo)
        else:
            bot.send_message(message.chat.id, "Виберіть число 1-10")
            bot.register_next_step_handler(message, get_user_photo)
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано", reply_markup=del_markup)


def get_user_text(message, user_photo):
    if message.text != cance_text:
        user_text = message.text
        bot.send_message(message.chat.id, "Тепер напиши юзернейм кому відправити (@username без @)",
                         reply_markup=markup_cance)
        bot.register_next_step_handler(message, get_user_for, user_photo, user_text)
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано", reply_markup=del_markup)


def get_user_for(message, user_photo, user_text):
    if message.text != cance_text:
        user_for = message.text
        bot.send_message(message.chat.id, "Тепер підпишись якось (можна як завгодно)",
                         reply_markup=markup_cance)
        bot.register_next_step_handler(message, get_user_from, user_photo, user_text, user_for)
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано", reply_markup=del_markup)


def get_user_from(message, user_photo, user_text, user_for):
    if message.text != cance_text:
        user_from = message.text
        log_deb(f"username: {message.from_user.username}")
        log_deb(f"user_text: {user_text}")
        log_deb(f"user_for: {user_for}")
        log_deb(f"user_from: {user_from}")
        try:
            valentine = photos_two.get_image(user_photo, user_text, user_for, user_from)
            img = open(valentine, 'rb')
            bot.send_photo(message.chat.id, img)
            log_inf("SUCCES CREATE")
            bot.send_message(message.chat.id, "Відправляти?", reply_markup=tf_markup)
            bot.register_next_step_handler(message, send_valentine, user_for, valentine)
        except Exception as ex:
            print(ex)
            log_err("ERROR CREATE")
            bot.send_message(message.chat.id, "Виникла помилка при створенні", reply_markup=del_markup)


def send_valentine(message, user_for, valentine):
    if message.text == Yes_text:
        bot.send_message(message.chat.id, "Валентинчик побіг відправляти", reply_markup=del_markup)
        try:
            send.sender(user_for, valentine)
            bot.send_message(message.chat.id, "Вашу валентинку відправлено!")
            log_inf("SUCCES SEND")
        except Exception as ex:
            print(ex)
            log_err("ERROR SEND")
            bot.send_message(message.chat.id, "Виникла помилка при передачі")
    else:
        bot.send_message(message.chat.id, "Формування валентинки скасовано", reply_markup=del_markup)


if __name__ == "__main__":
    bot.polling(none_stop=True)
