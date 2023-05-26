from apiflask import APIFlask

app = APIFlask(__name__)

@app.get('/')
def say_hello():
    return {'message': 'Hello!'}