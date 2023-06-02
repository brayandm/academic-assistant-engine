from celery import Celery

from ..config import RESULT_BACKEND, CELERY_BROKER_URL

celery = Celery(
    "engine",
    backend=RESULT_BACKEND,
    broker=CELERY_BROKER_URL,
    include=["engine.server.tasks"],
)
