import json
import requests
from .output_schemas import TranslationResult
from ..config import ENGINE_API_TOKEN
from ..redis import redis


def on_translation_completed(task, _, task_id, task_args, task_kwargs, *args, **kwargs):
    hook = task_kwargs.get("hook", None)
    if not hook:
        return
    schema = TranslationResult()
    result = json.loads(redis.get(f"celery-task-meta-{task_id}").decode("utf-8"))[
        "result"
    ]

    data = {"task_id": task_id, "status": "SUCCESS", "result": result, "ai_models": []}

    requests.post(
        hook,
        json=schema.dump(data),
        headers={"X-API-Key": ENGINE_API_TOKEN},
    )


def on_translation_failed(task, _, task_id, task_args, task_kwargs, *args, **kwargs):
    hook = task_kwargs.get("hook", None)
    if not hook:
        return
    schema = TranslationResult()

    data = {
        "task_id": task_id,
        "status": "FAILED",
        "result": {"text": ""},
        "ai_models": [],
    }

    requests.post(
        hook,
        json=schema.dump(data),
        headers={"X-API-Key": ENGINE_API_TOKEN},
    )
