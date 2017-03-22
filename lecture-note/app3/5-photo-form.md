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

## registration/login.html 수정

next parameter를 전달하기 위해서 아래 부분을 수정합니다. 

next parameter의 값은 아래와 같은 url을 통해서 전달 받을 수 있습니다. 

`view-source:http://127.0.0.1:8000/accounts/login/?next=/kilogram/upload` 
이 경우 next에는 `kilogram/upload` 값이 들어갑니다. 

```
<input type="hidden" name="next" value="{{next}}" />
``` 