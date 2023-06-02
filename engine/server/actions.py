from ..openai import api


def translate(task_id, user, original_language, target_language, text_type, text):
    response = api.chat_completion(
        user,
        task_id,
        "gpt-3.5-turbo",
        [
            {
                "role": "user",
                "content": f"Translate the following text from {original_language} to {target_language} keeping the {text_type} format:\n\n{text}",
            },
        ],
    )

    return {"text": response["choices"][0]["message"]["content"]}
