import os

AMQP = {
    "username": os.environ.get("RABBITMQ_USER", "rabbitmq_usr"),
    "password": os.environ.get("RABBITMQ_PASSWORD", "rabbitmq_password"),
    "host": os.environ.get("RABBITMQ_HOST", "rabbitmq"),
    "port": os.environ.get("RABBITMQ_PORT", "5672"),
    "vhost": os.environ.get("RABBITMQ_VHOST", "judge_vhost"),
}

CELERY_BROKER_URL = (
    "amqp://{username}:{password}@{host}:{port}/{vhost}".format(**AMQP),
)
