import sys
from django.conf.urls import url
# from django.core.urlresolvers import resolve # for django 1
from django.urls import reverse
from django.conf import settings

def hoge(request):
    return 'here is hoge'

def index(request):
    return 'here is index'

urlpatterns = [
    url(r'^$', index),
    url(r'hoge$', hoge),
]

def handler(request):
    if not settings.configured:
        settings.configure(
            ALLOWED_HOSTS=["*"],
            DEBUG=True,
            ROOT_URLCONF=__name__,
            MIDDLEWARE_CLASSES=(
                'django.middleware.common.CommonMiddleware',
            )
        )

    return reverse('index')
    # return resolve('index')
