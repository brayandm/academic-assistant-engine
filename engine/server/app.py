from apiflask import APIFlask, HTTPTokenAuth
from . import tasks
from .input_schemas import TextToTranslate
from ..config import ENGINE_API_TOKEN

app = APIFlask(__name__)

auth = HTTPTokenAuth(scheme="ApiKey", header="X-API-Key")


@auth.verify_token
def verify_token(token):
    print(token)
    if token == ENGINE_API_TOKEN:
        return token
    print("Invalid token")


@app.get("/")
def say_hello():
    return {"task_id": tasks.add.delay().id}


@app.post("/translate")
@app.auth_required(auth)
@app.input(TextToTranslate)
def translate(data):
    return {"task_id": tasks.translate.delay(data, hook=data.get("hook", None)).id}
