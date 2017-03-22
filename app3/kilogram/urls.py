from django.conf.urls import url
from . import views

app_name ='kilogram'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^upload$', views.upload, name = 'upload')
]
