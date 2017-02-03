# static file 연동하기

참고링크: https://docs.djangoproject.com/en/1.10/howto/static-files/

## css 파일 만들기 

- polls/static/polls/style.css
```css
a {
    color: red;
    text-decoration: none;
}

body {
    background: white url("images/background.gif") no-repeat right bottom;
}
```
## css 파일 적용 
```html
{% load static %}

<link rel="stylesheet" type="text/css" href="{% static 'polls/style.css' %}" />
```

## settings.py 수정
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

## collectstatic 명령 수행 및 변경사항 확인 
```
$ python manage.py collectstatic
```

# custom admin template

## settings.py 수정
```python
INSTALLED_APPS = [
    'polls',
    'django.contrib.admin',
    # ...
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # ...
    }
]
```

## polls/templates/admin/base_site.html 생성
```
{% extends "admin/base.html" %}

{% block title %}{{ title }} | {{ site_title|default:_('Django site admin') }}{% endblock %}

{% block branding %}
<h1 id="site-name"><a href="{% url 'admin:index' %}">{{ site_header|default:_('Django administration') }}</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}
```
# 템플릿 확장하기
- templates/polls/base.html 생성
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
  <title>Django Polls Example</title>

  <!-- Bootstrap -->
  <link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">

  <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
  <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
  <!--[if lt IE 9]>
  <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
  <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
  <![endif]-->
</head>
<body>
  <div class="container">
    <nav class="navbar navbar-default">
      <div class="container-fluid">
        <div class="navbar-header">
          <span class="navbar-brand">Polls Example</span>
        </div>
        <ul class="nav navbar-nav">
          <li><a href = "{% url 'polls:index' %}">투표</a></li>
          <li class="navbar-right"><a href = "{% url 'admin:index' %}">관리자</a></li>
        </ul>
      </div>
    </nav>
    <div>
      {% block content %}
      {% endblock %}
    </div>
  </div>
  <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
  <!-- Include all compiled plugins (below), or include individual files as needed -->
  <script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js></script>
  </body>
  </html>
```

## 나머지 페이지들 수정
```html
{% extends 'polls/base.html' %}

{% block content %}
<div class="jumbotron">
    <!-- 
        ohter html here
    -->
{% endblock content %}
``` 