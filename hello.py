from flask import Flask, redirect
from werkzeug.routing import RequestRedirect, MethodNotAllowed, NotFound

app = Flask(__name__)

def get_view_function(url, method='GET'):
    """Match a url and return the view and arguments
    it will be called with, or None if there is no view.
    """

    adapter = app.url_map.bind('localhost')

    try:
        match = adapter.match(url, method=method)
    except RequestRedirect as e:
        # recursively match redirects
        return get_view_function(e.new_url, method)
    except (MethodNotAllowed, NotFound):
        # no match
        return None

    try:
        # return the view function and arguments
        return app.view_functions[match[0]], match[1]
    except KeyError:
        # no view is associated with the endpoint
        return None


def hello_world(request):
    # return redirect()
    return get_view_function(request['path'])[0]()


@app.route('/')
def index():
    return f'here is index'


@app.route('/hoge')
def hoge():
    return f'hoge!'


if __name__ == '__main__':
    request = {'path': 'hoge'}
    print(hello_world(request))
