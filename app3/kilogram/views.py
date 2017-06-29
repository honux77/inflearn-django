from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import UploadForm, UserForm, ProfileForm
from .models import Profile
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

@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    photos = user.photo_set.filter(is_public=True)[:20]
    context = {"profile_user": user, "photos": photos}
    return render(request, 'kilogram/profile.html', context)


class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)

        user_form = UserForm(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
        })

        if hasattr(user, 'profile'):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'nickname': profile.nickname,
                'profile_photo': profile.profile_photo,
            })
        else:
            profile_file = ProfileForm()

        return render(request, 'kilogram/profile_update.html',
            {"user_form": user_form, "profile_form": profile_form})

    def post(self, request):
        pk = request.user.pk
        u = User.objects.get(id=pk)
        user_form = UserForm(request.POST, instance=u)

        if (user_form.is_valid()):
            user_form.save()

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES,
                instance=profile)
        else:
            profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = u
            profile.save()

        return redirect('kilogram:profile', pk)
