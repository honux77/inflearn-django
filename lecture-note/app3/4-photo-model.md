# 이미지 업로드 구현하기

## media url 설정하기

- mysite/settings.py 수정

```
# Media files
MEDIA_URL = '/files/'
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
    thumname_image = models.ImageField(blank = True)
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

