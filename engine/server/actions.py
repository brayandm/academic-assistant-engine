import time
import random
from ..openai import api


def translate(task_id, data):
    time.sleep(3)
    rd = random.randint(0, 1)
    if rd == 0:
        raise Exception("test")

    response = api.chat_completion(
        task_id,
        "gpt-3.5-turbo",
        [
            {
                "role": "user",
                "content": f"Translate this text in spanish: {data['text']}",
            },
        ],
    )

    return {"text": response["choices"][0]["message"]["content"]}
