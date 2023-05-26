from celery import Celery

from .config import CELERY_BROKER_URL

app = Celery(
    "tasks",
    broker=CELERY_BROKER_URL,
)


@app.task
def add(x, y):
    return x + y
