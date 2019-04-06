from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world(request):
    return f'Hello World!'


@app.route('/hoge')
def hoge(request):
    return f'hoge!'
