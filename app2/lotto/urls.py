from django.conf.urls import url
from django.contrib import admin
from lotto import views

app_name = 'lotto'

urlpatterns = [
    url(r'^lotto/$', views.index, name='lotto'),
    url(r'^$', views.index, name='index'),
    url(r'^lotto/new/$', views.post, name = "new_lotto"),
    url(r'^lotto/(?P<lottokey>[0-9]+)/detail/$', views.detail, name='detail'),


]
