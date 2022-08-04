from PIL import Image, ImageDraw, ImageFont
import random

chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'


def get_image(user_photo, user_for, user_from):
    image = Image.open(user_photo)

    font = ImageFont.truetype('arial.ttf', 220)
    drawer = ImageDraw.Draw(image)
    drawer.text((300, 2300), f"Від: {user_from}\nДля: {user_for}", font=font, fill='black')

    name = ''
    for i in range(12):
        name += random.choice(chars)
    full_name = f"valentines/{name}.jpg"
    image.save(full_name)
    return full_name
