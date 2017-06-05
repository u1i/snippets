# run with the following command:
# gunicorn -w 4 --bind=0.0.0.0:80 hello:app
# (assuming that the file is called hello.py)

import bottle
from bottle import route, run

@route('/')
def index():
    return '<h1>Hello Bottle!</h1>'

if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)

app = bottle.default_app()
