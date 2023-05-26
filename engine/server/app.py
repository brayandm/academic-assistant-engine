from apiflask import APIFlask
from . import tasks
from .schemas import TextToTranslate

app = APIFlask(__name__)


@app.get("/")
def say_hello():
    return {"taskId": tasks.add.delay().id}


@app.post("/translate")
@app.input(TextToTranslate)
def translate(data):
    return {"taskId": tasks.translate.delay(data).id}
