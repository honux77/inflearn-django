## 기본 view 및 템플릿 수정

- mysite/urls.py 및 kilogram/urls.py 수정

- mysite/urls.py
```python
from django.contrib.auth.decorators import login_required
  # ...
  url(r'^$', login_required(kilogram_views.IndexView.as_view()), name = 'root'),

```

- kilogram/urls.py

```python
from django.contrib.auth.decorators import login_required

  url(r'^$', login_required(views.IndexView.as_view()), name = 'index'),
```

- kilogram/views.py 수정

```python
class IndexView(ListView):
    # model = Photo
    context_object_name = 'user_photo_list'
    paginate_by = 2

    def get_queryset(self):
        user = self.request.user
        return user.photo_set.all().order_by('-pub_date')
```

- index.html 을 photo_list.html로 이름 변경

- photo_list.html 편집
```html
{% extends 'kilogram/base.html' %}
{% block content %}

<p> <a class="btn btn-primary" href="{% url 'kilogram:upload'%}">업로드</a></p>

  {% if user_photo_list %}
  {% for photo in user_photo_list %}
  <div class="panel panel-default" align="center">
    <div class="panel-heading"><h4>{{photo.owner.username}}</h4></div>
    <div class="panel-body">
      {% if photo.image.width > 800 %}
      <p><img src = '{{photo.image.url}}' width='600' /> <br>
        {% else %}
        <p><img src = '{{photo.image.url}}' /> <br>
          {% endif %}
          {{photo.comment}}</p>
      </div>
    </div>
      {% endfor %}
      {% else %}
      <h4>아직 사진이 없네요. 첫번째 사진을 업로드하세요!</h4>
      {% endif %}

    <!-- pagenation nav -->
    {% if is_paginated %}
    <nav aria-label="...">
        <ul class="pager">
          {% if page_obj.has_previous %}
          <li><a href="{%url 'kilogram:index'%}?page={{ page_obj.previous_page_number }}">이전</a></li>
          {% endif %}
          <li> <a href="#">페이지 {{ page_obj.number }} / {{ page_obj.paginator.num_pages }} </a></li>
          {% if page_obj.has_next %}
          <li>
            <a href="{%url 'kilogram:index'%}?page={{ page_obj.next_page_number }}">다음</a>
          </li>
          {% endif %}
        </ul>
    </nav>
    {% endif %}

{% endblock %}

```


## 참고링크
- https://docs.djangoproject.com/en/1.10/ref/models/fields/
- https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/