from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^lotto/', views.index, name = 'lotto_view')
]
