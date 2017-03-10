from django.shortcuts import render
from django.shortcuts import redirect

from .forms import CreateUserForm
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'kilogram/index.html'

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm
    success_url = reverse_lazy('create_user_done')

class ResisteredView(TemplateView):
    template_name = 'registration/done.html'
