from ..celery.app import celery


@celery.task(bind=True)
def add(task):
    return {"taskid": task.request.id, "result": {"message": "Hello!"}}
