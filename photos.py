import os
import random

folder = "photos"


def get_photo():
    arr = os.listdir(folder)
    photo = random.choice(arr)
    return f"{folder}/{photo}"
