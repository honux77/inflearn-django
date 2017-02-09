# app1과 app2 합치기
## app1 전체 및 mysite/urls.py 복사해 오기
탐색기를 이용해 작업을 하는 편이 안전
```bash
$ cd app2
$ cp -a ../app1/lotto/ lotto
$ cp ../app1/mysite/urls.py lotto/
```
## 몇 가지 고치기
- app2/mysite/settings.py

```python
INSTALLED_APPS = [
    'polls',
    'lotto',
    # ...
```
- app2/mysite/urls.py
```python
from django.conf.urls import url, include
from django.contrib import admin
from polls import views

urlpatterns = [
    url(r'^$', views.main, name = 'main'),
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^lotto/', include('lotto.urls'))
]
```
- app2/lotto/urls.py
```python
from django.conf.urls import url
from . import views

app_name = 'lotto'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new/$', views.post, name = "new_lotto"),
    url(r'^(?P<lottokey>[0-9]+)/detail/$', views.detail, name='detail'),
]

```

- app2/lotto/views.py 

```python
  def post(request):
            # ...
            return redirect('lotto:index')

```

- app2/lotto/templates/lotto/default.html
```html
    <h2> <a href="{% url 'lotto:new_lotto'%}">
    <!-- ... -->
    <h2><a href="{% url 'lotto:detail' lottokey=lotto.pk %}">{{lotto.text}}</a></h2>
```


- a/app2/polls/templates/polls/base.html
```html
  <li><a href = "{% url 'lotto:index' %}">로또</a></li>
```

## migrate
```bash
$ python manage.py migrate
```
