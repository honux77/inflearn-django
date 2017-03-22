# 이미지 업로드 구현하기

## media url 설정하기

- mysite/settings.py 수정

```
# Media files
MEDIA_URL = '/p/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
```

## photo model 생성하기

- kilogram/model.py 수정

```python
from django.db import models
from django.conf import settings
# Create your models here.

def user_path(instance, filename):
    from random import choice
    arr = [choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(8)]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    # file will be uploaded to MEDIA_ROOT/user_<id>/<random>
    return '%s/%s.%s' % (instance.owner.username, pid, extension)

class Photo(models.Model):
    image = models.ImageField(upload_to = user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    thumbnail_image = models.ImageField()
    comment = models.CharField(max_length = 255)
    pub_date = models.DateTimeField(auto_now_add = True)
```

- pillow 설치

ImageField 사용시 에러가 발생하므로 pillow 패키지를 설치한다.

```
$ pip install pillow
```
-  migrate 수행
```
$ python manage.py makemigrations
$ python manage.py migrate
```

- admin.py 수정 및 admin을 통한 확인
```
from .models import Photo

# Register your models here.
admin.site.register(Photo)
```

## media url 을 static url로 설정하기

- **mysite/urls.py 수정**

```
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

```

## upload form 작성

- kilogram/forms.py 추가
```
class UploadForm(forms.ModelForm):
    comment = forms.CharField(max_length = 255)
    class Meta:
        model = Photo
        exclude = ('thumbnail_image','owner')
```

## photo upload url 및 view 작성

- kilogram/urls.py 수정
```
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^upload$', views.upload, name = 'upload'),
]
```

- kilogram/views.py 수정

```
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Photo

@login_required
def upload(request):
    if request.method == "POST":
        # save data
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit = False)
            photo.owner = request.user
            form.save()
            return redirect('kilogram:index')

    form = UploadForm()
    return render(request, 'kilogram/upload.html', {'form': form})
```

## template 생성 및 수정

- upload.html 생성

```
{% extends 'kilogram/base.html' %}
{% block content %}

<h1>Kilogram Image Upload</h1>

<form action="{% url 'kilogram:upload' %}" method="post" enctype="multipart/form-data">
  {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="Upload" />
</form>
{% endblock %}
```

- admin을 통한 upload 확인
- shell을 통한 upload 확인

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
