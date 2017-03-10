# 기본 설정 및 프로젝트 초기화

## start project and app
```
$ python manage.py startapp kilogram
```

## settings.py 수정
```python
INSTALLED_APPS = [
    'kilogram',
    #...

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```
## model

아직까지는 특별히 생성 또는 수정할 model이 없습니다.

## kilogram/urls.py 생성
```
from django.conf.urls import url
from . import views

app_name = 'kilogram'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
]
```

## (new!) mysite/urls.py 수정
파이썬 기본 문법인 `as`를 적용해서 views를 구별 가능하도록 합니다.

```
from django.conf.urls import url, include
from django.contrib import admin
from kilogram import views as kilogram_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', kilogram_views.IndexView.as_view(), name = "root"),
    url(r'^kilogram/', include('kilogram_views.urls')),
]
```

## (new!) kilogram/views.py 수정


간단히 템플릿을 적용하기 위해서 generic view인 TemplateView를 사용했습니다.

```
from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'kilogram/index.html'
```

## 기본 템플릿 작성
- base.html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Kilogram</title>

  <!-- Bootstrap -->
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

  {% load static %}
  <link rel="stylesheet" type="text/css" href="{% static 'kilogram/style.css' %}" />

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body>
  <nav class="navbar navbar-default navbar-static-top">
  <div class="container-fluid">
    <!-- Brand and toggle get grouped for better mobile display -->
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="{% url 'kilogram:index' %}"> <span class="glyphicon glyphicon-camera"> </span> Kilogram </a>
    </div>

    <!-- Collect the nav links, forms, and other content for toggling -->
    <div class="collapse navbar-collapse">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="{%url 'login' %}"> <span class="glyphicon glyphicon-user"></span> Login</a></li>
        <li><a href="{% url 'logout' %}">Logout</a></li>
        <li><a href="{% url 'admin:index' %}">Admin</a></li>
      </ul>
    </div><!-- /.navbar-collapse -->
  </div><!-- /.container-fluid -->
</nav>
  <div class="container">
    <div>
      {% block content %}
      {% endblock %}
    </div>
  </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
</body>
</html>
```

- index.html

```html
{% extends 'kilogram/base.html' %}
{% block content %}

<h1>Kilogram Main Page</h1>

{% endblock content %}
```
