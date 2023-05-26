from apiflask import APIFlask
from . import tasks

app = APIFlask(__name__)


@app.get("/")
def say_hello():
    tasks.add.delay(1, 2)
    return {"message": "Hello!"}
