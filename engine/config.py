import os

AMQP = {
    "username": os.environ.get("RABBITMQ_USER"),
    "password": os.environ.get("RABBITMQ_PASSWORD"),
    "host": os.environ.get("RABBITMQ_HOST"),
    "port": os.environ.get("RABBITMQ_PORT"),
    "vhost": os.environ.get(
        "RABBITMQ_VHOST",
    ),
}

REDIS = {
    "password": os.environ.get("REDIS_PASSWORD"),
    "host": os.environ.get("REDIS_HOST"),
    "port": os.environ.get("REDIS_PORT"),
    "db": os.environ.get("REDIS_DB_NUMBER"),
}

CELERY_BROKER_URL = (
    "amqp://{username}:{password}@{host}:{port}/{vhost}".format(**AMQP),
)

RESULT_BACKEND = "redis://:{password}@{host}:{port}/{db}".format(**REDIS)

ENGINE_API_TOKEN = os.environ.get("ENGINE_API_TOKEN")
