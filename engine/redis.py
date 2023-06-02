from redis import Redis
from .config import REDIS

redis = Redis(**REDIS)
