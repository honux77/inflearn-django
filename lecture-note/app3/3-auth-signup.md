# auth - 회원 가입 구현하기 

## model
역시 모델의 수정은 필요 없습니다.

## settings/urls.py 수정 

장고의 auth.urls에는 회원 가입 url이 따로 없기 때문에 구현해 주어야 합니다. 추후에 settings.py에 관련 속성 값들도 몇가지 추가를 해 줄 예정입니다.

```
urlpatterns = [
  url(r'^accounts/signup/$', kilogram_views.CreateUserView.as_view(), name = 'signup'),
  url(r'^accounts/login/done$', kilogram_views.ResisteredView.as_view(), name = 'create_user_done')
]
```

## 회원 가입 폼 클래스 만들기 

회원가입 폼을 만드는 방법은 여러가지가 있을 수 있는데, 그 중 가장 간단한 장고에서 제공하는 UserCreationForm(django.contrib.auth.forms.UserCreationForm)을 사용합니다.
다만 요즘 대부분의 사이트에서 필수적으로 받는 이메일도 입력받기 위해서 추가적으로 구현을 더 했습니다. 

내용이 어렵다면 넘어가셔도 됩니다. 

- forms.py 생성 

```python
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

## CreateUserForm을 활용해서 CreateUserView 만들기

View 는 generic view 중 폼을 이용해 오브젝트를 생성하는 CreateView를 사용합니다.
reverse_lazy는 reverse와 같은 기능인데 generic view에서 주로 사용한다고 이해하시면 됩니다.

- views.py 수정

```
from django.views.generic.edit import CreateView
# from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy

class CreateUserView(CreateView):
    template_name = 'registration/signup.html'
    form_class =  CreateUserForm
    # form_class = UserCreationForm
    success_url = reverse_lazy('create_user_done')

class RegisteredView(TemplateView):
    template_name = 'registration/signup_done.html'
```

## template 생성

RegisteredView에서 사용할 template을 만들어 줍니다.


## 참고 링크
- https://docs.djangoproject.com/en/1.10/ref/urlresolvers/
- https://docs.djangoproject.com/en/1.10/topics/auth/default/
