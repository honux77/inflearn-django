# App2 Tutorial 1

## 준비
- virtualenv 활성화
## 프로젝트 생성:
```bash
$ django-admin startproject mysite
```
## 서버 시작 및 settings.py 수정
```bash
$ python manage.py runserver
$ python manage.py ryunserver 8080
```
## 앱 생성
```python
$ python manage.py startapp polls
```
## 첫번째 뷰
- views.py 수정
``` python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
- polls/urls.py 생성 (새로운 방법)
``` python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
- mysite/urls.py 수정 (새로운 방법)
``` python
    url(r'^polls/', include('polls.urls')),
```
