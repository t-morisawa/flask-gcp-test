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

仮にこうして`/hoge`を呼んでも`hoge`は呼ばれず`Hello World!`が呼び出される。

なぜならwsgiが動いていないからである。


## wsgi

仕様書はここを読むこと

https://www.python.org/dev/peps/pep-3333/

あるいはここのチュートリアルでも可

http://wsgi.tutorial.codepoint.net/intro

# メモ

 - サーバレスでWebアプリケーションサーバを使う方法を考える。
 - ngrok(リバースプロキシ)を使う手もあるらしい。
 - ステートフルWEBアプリ
