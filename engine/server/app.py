from apiflask import APIFlask
from . import tasks

app = APIFlask(__name__)


@app.get("/")
def say_hello():
    return {"taskId": tasks.add.delay().id}
