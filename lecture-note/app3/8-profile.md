# 프로파일 페이지 만들기

## Profile 모델 추가하기

- User 모델 확장하는 방법과 OneToOne 관계를 이용하는 방법 중 쉬운 방법을 사용한다.
- kilogram/models.py 추가

> 기존 소스에서 thumbnail_image에 오타가 있어서 수정함

```python
class Photo(models.Model):
    # ...
    thumbnail_image = models.ImageField(blank = True)
    # ...

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    profile_photo = models.ImageField(blank=True)
    nickname = models.CharField(max=64)
```

## admin.py에 모델 추가
- User에 모델과 프로파일이 한꺼번에 보이도록 수정
- 기존 앱을 만들 때 사용했던 `StackedInline`을 사용한다.
- UserAdmin을 커스터마이즈하기 위해서 상속받아서 구현

```
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Photo
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Register your models here.
admin.site.register(Photo)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
```

## view 만들기
- 두 개의 모델(User, Profile)을 하나의 템플릿에 표시해야 한다.
- User에서 1:1 관계로 Profile을 참조할 수 있으므로 기본 detail view를 상속받아서 만들 수 있다.
- 다만 객체 이름이 `User` 로 넘어오는데 기본으로 있는 현재 User 정보를 담은 오브젝트와 이름이
같으므로 변경이 필요하다.

```
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView

class ProfileView(DetailView):
    context_object_name = 'profile_user'
    model = User
    template_name = 'kilogram/profile.html'
```
## kilogram/urls.py 수정

```python
url(r'^profile/(?P<pk>[0-9]+)/$', login_required(views.ProfileView.as_view()),
    name='profile'),

```

## template 만들기

- css를 업데이트한다. 프로파일 이미지를 둥글게 처리

kilogram/static/kilogram/style.css

```css
.round {
    border-radius: 50%;
}
```
- 프로필 사진이 없을 경우 대신 사용할 사진 업로드
kilogram/satic/kilogram/images/photo.jpg


- profile 페이지용 템플릿
- static file을 이용하므로 `load staticfiles` 가 꼭 있어야 함

templates/kilogram/profile.html

```
{% extends 'account/base.html' %}
{% block content %}

{% load staticfiles %}

<div class="row">
    <div class="col-xs-6 col-md-3">
        {% if profile_user.profile.profile_photo %}
        <img class="round" src="{{profile_user.profile.profile_photo.url}}" width="200"> <br>
        {% else %}
        <img class="round" src="{% static 'kilogram/images/photo.jpg' %}" width="200"> <br>
        {% endif %}
    </div>

    <div class="col-xs-6 col-md-3">
        {% if profile_user.profile.nickname %}
        <h2>{{profile_user.profile.nickname}}</h2>
        {% endif %}
        {% if user == profile_user %}
        <a href="#">
            <button type="button" class="btn btn-default">프로필 편집</button></a></h2>
        {% endif %}
        <h3> username: {{profile_user.username}} <br>
            {% if profile_user.first_name is not None %}
            name: {{profile_user.first_name}} {{profile_user.last_name}} <br>
            {% endif %}
        </h3>
    </div>
</div>

{% endblock %}

```

## kilogram/templates/kilogram/base.html 수정
```
-        <li><a href="#"> <span class="glyphicon glyphicon-heart"></span> {{user.username}}</a></li>
+        <li><a href="{% url 'kilogram:profile' user.pk %}"> <span class="glyphicon glyphicon-heart"></span> {{user.username}}</a></li>
```
