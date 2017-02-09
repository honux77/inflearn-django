from django.conf.urls import url
from . import views

app_name = 'lotto'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post, name = "new_lotto"),
    url(r'^(?P<lottokey>[0-9]+)/detail/$', views.detail, name='detail'),
]
