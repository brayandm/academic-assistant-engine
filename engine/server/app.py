from apiflask import APIFlask, HTTPTokenAuth
from . import tasks
from .schemas import TextToTranslate
from .config import API_TOKEN

app = APIFlask(__name__)

auth = HTTPTokenAuth(scheme="ApiKey", header="X-API-Key")


@auth.verify_token
def verify_token(token):
    print(token)
    if token == API_TOKEN:
        return token
    print("Invalid token")


@app.get("/")
def say_hello():
    return {"taskId": tasks.add.delay().id}


@app.post("/translate")
@app.auth_required(auth)
@app.input(TextToTranslate)
def translate(data):
    return {"taskId": tasks.translate.delay(data).id}
