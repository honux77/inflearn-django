#　profile update 페이지 만들기

##　form.py 수정
```
from .models import Photo, Profile

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', ]


class ProfileForm(forms.ModelForm):
    # nickname = forms.CharField(max_length=255)
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ['nickname', 'profile_photo']
```

## views.py 수정

- 불필요한 view와 import는 제거한다.
- ProfileUpdateView는 기본 View를 확장해서 만든다.
- 두 개의 모델을 하나의 form에서 업데이트를 하는 방식으로 구현하였다.
- 이전 값이 들어가도록 구현한다.
- 새로운 값의 삽입이 아니라, update가 가능하도록 구현한다.

```python
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .forms import UploadForm, ProfileForm, UserForm
from .models import Profile

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
                'nickname': user.profile.nickname,
                'profile_photo': profile.profile_photo,
            })
        else:
            profile_form = ProfileForm()

        return render(request, 'kilogram/profile_update.html',
                      {"user_form": user_form, "profile_form": profile_form})

    def post(self, request):
        pk = request.user.pk
        u = User.objects.get(id=pk)
        user_form = UserForm(request.POST, instance=u)

        if user_form.is_valid():
            user_form.save()

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        else:
            profile_form = ProfileForm(request.POST, request.FILES)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = u
            profile.save()

        return redirect('kilogram:profile', pk)
```

## urls.py 수정
```
url(r'^profile/update/$', login_required(views.ProfileUpdateView.as_view()),
  name='profile_update'),
```
## templates 수정

kilogram/templates/kilogram/profile.html 
```
        {% if user == profile_user %}
        <a href="{% url 'kilogram:profile_update' %}">
```
## templates 생성

kilogram/templates/kilogram/profile_update.html
```
{% extends 'account/base.html' %}
{% block content %}

<h1>{{user.username}} Profile Update</h1>

    {% if error_msg %}
    <div class="alert alert-warning alert-dismissible" role="alert">
    <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button>
    <strong>Error</strong> {{error_msg}}
    </div>
    {% endif %}

    <form action="" method="post" enctype="multipart/form-data">{% csrf_token %}
    {{ user_form.as_p }}
    {{ profile_form.as_p }}
    <input type="submit" value="Update" />
</form>
</p>

{% endblock %}

```