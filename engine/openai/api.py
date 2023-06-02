import os
import openai
import json
from ..redis import redis

openai.api_key = os.environ.get("OPENAI_API_KEY")


def chat_completion(user, task_id, model, messages):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        user=user,
    )

    model = {
        "name": model,
        "option": "chat-completion",
        "usage_type": "tokens",
        "usage": response["usage"]["total_tokens"],
    }

    redis.rpush(f"openia-models-meta-{task_id}", json.dumps(model))

    return response
