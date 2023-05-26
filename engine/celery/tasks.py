from celery import Celery

from .config import RESULT_BACKEND, CELERY_BROKER_URL

app = Celery(
    "tasks",
    backend=RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
)


@app.task
def add(x, y):
    return x + y
