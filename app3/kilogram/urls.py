from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name ='kilogram'

urlpatterns = [
    url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    url(r'^upload$', views.upload, name='upload'),
    url(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()), name='profile'),
    url(r'^profile/update/$', login_required(views.ProfileUpdateView.as_view()), name='profile_update'),

]
