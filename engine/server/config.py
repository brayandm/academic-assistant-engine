import os

API_TOKEN = os.environ.get("API_TOKEN")

REDIS = {
    "password": os.environ.get("REDIS_PASSWORD"),
    "host": os.environ.get("REDIS_HOST"),
    "port": os.environ.get("REDIS_PORT"),
    "db": os.environ.get("REDIS_DB_NUMBER"),
}
