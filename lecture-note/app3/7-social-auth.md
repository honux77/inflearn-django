# social-auth를 이용한 facebook login 구현하기 

## 패키지 설치

github에서 django auth로 검색 후 가장 많은 스타를 받은 프로젝트인 https://github.com/pennersr/django-allauth 를 사용하기로 결정

공식 문서는 https://django-allauth.readthedocs.io/en/latest/installation.html
서 볼 수 있습니다.

```
$ pip install django-allauth
```

## settings.py 수정 

TEMPLATES 부분을 수정합니다.
```python
TEMPLATES = [ 
#...
'context_processors': [
                # Already defined Django-related contexts here

                # `allauth` needs this from django
                'django.template.context_processors.request',
 ]
]

# for django-allauth
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

INSTALLED_APPS = (
    ...
    # The following apps are required:
    'django.contrib.auth',
    'django.contrib.sites',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # ... include the providers you want to enable:
    'allauth.socialaccount.providers.facebook',
    #'allauth.socialaccount.providers.github',
    #'allauth.socialaccount.providers.kakao',
]

SITE_ID = 1

```

# urls.py 수정 
```
urlpatterns = [
    # ...
    url(r'^accounts/', include('allauth.urls'),
    # ...
]
```

## migrate 수행
```
$ python manage.py migrate
```

## 페이스북 앱 생성
developer.facebook.com 을 이용해서 로그인 앱 생성
ID 및 키값 저장 

## admin 사이트를 이용한 레코드 추가
Site에 127.0.0.1:8000 추가
Social App 추가 

## url 링크 수정
기존의 링크들로 인해서 오류가 발생하는데 이것들을 수정해 주어야 한다. 
수정해 주어야 하는 url들은 브라우저에서 확인할 수 있다. 
registant/base.html 수정

## 템플릿 수정 
https://django-allauth.readthedocs.io/en/latest/templates.html
https://github.com/pennersr/django-allauth/tree/master/allauth/templates

account/base.html 생성
