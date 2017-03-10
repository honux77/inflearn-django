from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

from .forms import CreateUserForm
# Create your views here.

class IndexView(TemplateView):
    template_name = 'kilogram/index.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CreateUserForm
    # form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
