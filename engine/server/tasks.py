from ..celery.app import celery
from . import callbacks
from . import actions


@celery.task(bind=True)
def add(task):
    return {"task_id": task.request.id, "result": {"message": "Hello!"}}


@celery.task(
    bind=True,
    on_success=callbacks.on_translation_completed,
    on_failure=callbacks.on_translation_failed,
)
def translate(task, data, hook=None):
    return actions.translate(task.request.id, data)
