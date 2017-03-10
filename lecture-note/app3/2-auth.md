# 인증 구현하기

회원 가입, 로그인을 구현하도록 합니다.

## model

장고의 django.contrib.auth.models.User 를 그대로 사용합니다.
특별한 코딩은 필요하지 않습니다.

## auth url 추가하기

장고에 기본으로 내장된 인증 기능을 활용합니다. 회원 가입은 기본 url이 따로 없기 때문에 구현해 주어야 합니다. 추후에 settings.py에 관련 속성 값들도 몇가지 추가를 해 줄 예정입니다.

- settings/urls.py
```
urlpatterns = [
  url(r'^accounts/', include('django.contrib.auth.urls')),
  url(r'^accounts/signup/$', kilogram_views.CreateUserView.as_view(), name = 'signup'),
  url(r'^accounts/login/done$', kilogram_views.ResisteredView.as_view(), name = 'create_user_done')
]
```
auth.urls를 include 할 경우 아래와 같은 url들이 포함됩니다.

```
^login/$ [name='login']
^logout/$ [name='logout']
^password_change/$ [name='password_change']
^password_change/done/$ [name='password_change_done']
^password_reset/$ [name='password_reset']
^password_reset/done/$ [name='password_reset_done']
^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$ [name='password_reset_confirm']
^reset/done/$ [name='password_reset_complete']
```

## form 추가하기
회원가입 폼을 만드는 방법은 여러가지가 있을 수 있는데, 그 중 가장 간단한 장고에서 제공하는 UserCreationForm(django.contrib.auth.forms.UserCreationForm)을 사용합니다.
다만 요즘 대부분의 사이트에서 필수적으로 받는 이메일도 입력받기 위해서 추가적으로 구현을 더 했습니다.

- forms.py
```
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
```

## view 만들기
View 는 generic view 중 폼을 이용해 오브젝트를 생성하는 CreateView를 사용합니다.
reverse_lazy는 reverse와 같은 기능인데 generic view에서 주로 사용한다고 이해하시면 됩니다.

- views.py 수정

```
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy


class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm
    success_url = reverse_lazy('create_user_done')
```

## template 생성

필요한 3개의 url - login, signup, create_user_done 들이 사용할 template을 만들어 줍니다.

- registration/login.html


```
{% extends 'kilogram/base.html' %}
{% block content %}

{% if user.is_active %}
<h2> Welcome, {{user.username}} </h2>
<a href="%url 'logout' %">로그아웃</a>

{% else %}
{% if form.errors %}
<p>ID나 비밀번호가 일치하지 않습니다.</p>
{% endif %}

<form method="post" action="{% url 'login' %}">
{% csrf_token %}
<input type="hidden" name="next" value="" />
{{ form.as_p }}
<button type="submit">로그인</button>
</form>

{% endif %}

{% endblock %}
```

- base.html 수정

로그인 및 로그아웃 링크를 추가합니다. 로그인한 상태와 로그인하지 않은 상태에서 보여줄 링크도 변경합니다.

```html
<ul class="nav navbar-nav navbar-right">
  {% if user.is_active %}
  <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-heart"></span> {{user.username}}</a></li>
  <li><a href="{% url 'logout' %}">Logout</a></li>
  {% else %}
  <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-user"></span> Login</a></li>
  <li><a href="{% url 'admin:index' %}">Admin</a></li>
  {% endif %}
</ul>
```
- logged_out.html

로그아웃용 파일입니다. 템플릿 이름이 다르면 안 됩니다. 파일이름은 장고 소스의 auth.views.logout()을 보시면 확인할 수 있습니다.

```
{% extends 'kilogram/base.html' %}
{% block content %}

<h2> 잘 가요, 안녕. </h2>
<p><a href="{%url 'login'%}">다시 로그인하기</a></p>

{% endblock %}

```

## settings.py 수정

로그인후 리다이렉트 페이지는 기본적으로 /accounts/profile 로 지정되어 있는데 이를 변경합니다.
settings.py의 가장 아래에 아래 내용을 추가합니다.

```
# Auth settings
LOGIN_REDIRECT_URL = '/kilogram/'
```

## 참고 링크
- https://docs.djangoproject.com/en/1.10/ref/urlresolvers/
- https://docs.djangoproject.com/en/1.10/topics/auth/default/
