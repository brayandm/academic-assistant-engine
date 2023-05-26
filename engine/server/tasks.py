from ..celery.app import celery
from . import callbacks


@celery.task(bind=True)
def add(task):
    return {"taskId": task.request.id, "result": {"message": "Hello!"}}


@celery.task(bind=True, on_success=callbacks.on_translation_complete)
def translate(task, data, hook=None):
    return {"taskId": task.request.id, "text": "Translated text"}
