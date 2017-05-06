# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, run

@route('/')
def hello_world():
    return 'Hello from Bottle!'

application = default_app()

run(server='wsgiref', host="0.0.0.0", port=8080)



