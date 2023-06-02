import time
import random


def translate(data):
    time.sleep(5)
    rd = random.randint(0, 1)
    if rd == 0:
        raise Exception("test")
    return {"text": data["text"] + " translated"}
