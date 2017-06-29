from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import CreateUserForm, UploadForm
# Create your views here.

@login_required
def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')

    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form': form})

class IndexView(ListView):
    # model = Photo
    context_object_name = 'user_photo_list'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')

class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'kilogram/profile.html'
