
# urls.py 수정
```python
url(r'^lotto/$', views.index, name='index'),

# views 수정
```python
def index(request):
    return render(request, "lotto/default.html", {})
```

# template 만들기
`lotto/tempate/lotto/default.html` 로 만듭니다. 경로에 주의!

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <title>My Little Lotto</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css">
  <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css">
  <link href="//fonts.googleapis.com/css?family=Space+Mono" rel="stylesheet">
</head>

<body>
  <div class="page-header">
  <h1>My Lotto Page</h1>
  </div>
  <div class="container lotto">
    <h2>당첨 기원 (2)</h2>
    <p> last update:2000/1/1</p>
    <p> 1, 10, 15, 20, 30 </p>
  </div>
</body>
</html>
```
# 정적 파일 연동
lotto/static/css/lotto.css
```css
.page-header {
    background-color: #652596;
    margin-top: 0;
    padding: 20px 20px 20px 40px;
    font-family: 'Space Mono', monospace;
}

.page-header h1 {
  color: #FFFFFF;
}

.container {
  font-family: 'Space Mono', monospace;
}

.container h2 {
  color: #b9f442;
}
```

# lotto/templates/lotto.html 수정
```
{% load staticfiles %}
<link rel=”stylesheet” href=”{% static ‘css/lotto.css’ %}”>
```
# static 파일 수집 명령 실행
```
$ python manage.py collectstatic
```
