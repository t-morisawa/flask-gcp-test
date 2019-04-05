# FlaskをGCPで動かす

```
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world(request):
    return f'Hello World!'


@app.route('/hoge')
def hoge(request):
    return f'hoge!'
```

仮にこうして`/hoge`を呼んでもとしてもCloud Functionsの関数が呼び出されることはない。

なぜならwsgiが動いていないからである。

