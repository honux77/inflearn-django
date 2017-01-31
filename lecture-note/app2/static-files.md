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