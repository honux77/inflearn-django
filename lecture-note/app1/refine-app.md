# urls.py 추가

```python
url(r'^lotto/(?P<lottokey>[0-9]+)/$', views.detail, name = "detail"),
```

# views.py 수정

```
def detail(request, lottokey):
        lotto = GuessNumbers.objects.get(pk = lottokey)
        return render(request, "lotto/detail.html", {"lotto": lotto})
```

# lotto/detail.html 작성

```html
<!DOCTYPE html>
{% load staticfiles %}
<html lang="ko">
<head>
  <title>My Little Lotto</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
  <link href="//fonts.googleapis.com/css?family=Space+Mono" rel="stylesheet">
  <link rel="stylesheet" href="{% static 'css/lotto.css'%}">
</head>

<body>
  <div class="page-header">
  <h1>My Lotto Page</h1>
  </div>
  <div class="container lotto">
    <h2>{{lotto.text}}</h2>
    <p> by {{lotto.name}}</p>
    <p> {{lotto.update_date}}</p>
    <p> {{lotto.lottos|linebreaksbr}}</p>
  </div>
</body>
</html>
```

# default.html 수정

```html
<div class="page-header">
<h1>My Lotto Page
  <a href="{% url 'new_lotto' %}"><span class="glyphicon glyphicon-plus btn btn-default"></span></a></h1>
</div>

<h2><a href="{% url 'lotto_detail' lottokey=lotto.pk %}">{{lotto.text}}</a></h2>
```
