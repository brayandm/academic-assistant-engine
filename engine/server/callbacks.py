import json
import requests
from .output_schemas import TextTranslated
from .config import API_TOKEN
from .redis import redis


def on_translation_complete(task, _, task_id, task_args, task_kwargs, *args, **kwargs):
    hook = task_kwargs.get("hook", None)
    if not hook:
        return
    schema = TextTranslated()
    data = json.loads(redis.get(f"celery-task-meta-{task_id}").decode("utf-8"))[
        "result"
    ]
    print("###########################################################")
    print(
        "heregox",
        json.loads(redis.get(f"celery-task-meta-{task_id}").decode("utf-8"))["result"],
    )
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("###########################################################")
    print("herego0", redis.get(f"celery-task-meta-{task_id}").decode("utf-8"))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("###########################################################")
    print("herego1", task_id)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("###########################################################")
    print("herego2", data)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("###########################################################")
    print("herego3", schema.dump(data))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("###########################################################")
    requests.post(
        hook,
        json=schema.dump(data),
        headers={"X-API-Key": API_TOKEN},
    )
