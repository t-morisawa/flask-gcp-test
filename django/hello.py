# -*- coding:utf-8 -*-
# hello.py

import sys
from django.conf.urls import url
from django.http import HttpResponse


def index(request):
    import random
    return HttpResponse('Hello World. random={}\n'.format(random.random()))


def hoge(request):
    import random
    return HttpResponse('Hello Hoge World. random={}\n'.format(random.random()))


urlpatterns = [
    url(r'^$', index),
    url(r'^hoge$', hoge),
]

if __name__ == "__main__":
    from django.core import management
    from django.conf import settings

    settings.configure(
        ALLOWED_HOSTS=["*"],
        DEBUG=True,
        ROOT_URLCONF=__name__,
        MIDDLEWARE_CLASSES=(
            'django.middleware.common.CommonMiddleware',
        )
    )
    # using this via 'python server-example.py runserver'
    management.execute_from_command_line(sys.argv)

    # management.call_command('runserver')
