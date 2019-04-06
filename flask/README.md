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

## サンプルプログラム

Socket IOを使った例かと思いきやApp Engineで動かすサンプルだった。

https://github.com/insanj/funky

## AWS

公式でパッケージが用意されている。

https://aws.amazon.com/jp/blogs/compute/going-serverless-migrating-an-express-application-to-amazon-api-gateway-and-aws-lambda/

他にZappa, serverless-wsgiなどがある

## メモ

 - サーバレスでWebアプリケーションサーバを使う方法を考える。
 - ngrok(リバースプロキシ)を使う手もあるらしい。
 - ステートフルWEBアプリ

## `url_map`

Flaskのルート機能を直接持っているものでルーティングに使えるかもしれない？

http://flask.pocoo.org/docs/1.0/api/#flask.Flask.url_map

http://flask.pocoo.org/docs/1.0/api/#url-route-registrations

## 第二弾

```
from flask import Flask, redirect
app = Flask(__name__)


def hello_world(request):
    print(request.path)
    # return redirect()
    return redirect(request.path)

@app.route('/')
def index(request):
    return f'here is index'

@app.route('/hoge')
def hoge(request):
    return f'hoge!'
```

取得パスに基づいてリダイレクトさせればいいのでは？と思ったものの、ダメだった

このリダイレクトはそのままhttpリダイレクトなので無限にhello_worldが呼び出されてしまうため。

やりたいことは、urlからそれに対応するメソッドを引いてきて呼び出すということ。

https://stackoverflow.com/questions/38488134/get-the-flask-view-function-that-matches-a-url

