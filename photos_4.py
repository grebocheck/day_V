from PIL import Image, ImageDraw, ImageFont
import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

# Костиль для выбору колтору шрифта
photo_mass = {"templates/gachi/1.jpg": 'white',
              "templates/gachi/2.jpg": 'black',
              "templates/gachi/3.jpg": 'black',
              "templates/gachi/4.jpg": 'black',
              "templates/gachi/5.jpg": 'white',
              "templates/gachi/6.jpg": 'white',
              "templates/gachi/7.jpg": 'white',
              "templates/films/1.jpg": 'white',
              "templates/films/2.jpg": 'white',
              "templates/films/3.jpg": 'white',
              "templates/films/4.jpg": 'white',
              "templates/films/5.jpg": 'white',
              "templates/films/6.jpg": 'white',
              "templates/films/7.jpg": 'white',
              "templates/memes/1.jpg": 'black',
              "templates/memes/2.jpg": 'white',
              "templates/memes/3.jpg": 'white',
              "templates/memes/4.jpg": 'black',
              "templates/memes/5.jpg": 'white',
              "templates/memes/6.jpg": 'white',
              "templates/memes/7.jpg": 'white',
              "templates/nani/1.jpg": 'white',
              "templates/nani/2.jpg": 'white',
              "templates/nani/3.jpg": 'white',
              "templates/nani/4.jpg": 'white',
              "templates/nani/5.jpg": 'white',
              "templates/nani/6.jpg": 'white',
              "templates/nani/7.jpg": 'white',
              }


def get_image(user_photo, user_for, user_from):
    image = Image.open(user_photo)

    font = ImageFont.truetype('arial.ttf', 220)
    drawer = ImageDraw.Draw(image)
    drawer.text((300, 2300), f"Від: {user_from}\nДля: {user_for}", font=font, fill=photo_mass[user_photo])

    name = ''
    for i in range(12):
        name += random.choice(chars)
    full_name = f"valentines/{name}.jpg"
    image.save(full_name)
    return full_name
