# 프로파일에 썸네일 추가하기

## 필요 패키지 설치

- 여러가지 방법이 있지만 가장 쉬워 보이는(https://github.com/jazzband/sorl-thumbnail) 사용
- 그 외 https://github.com/matthewwithanm/django-imagekit 도 쉽고 좋아 보임
- 2017/6/29 일 현재 sorl thumbnail은 pip로 설치할 경우 오류가 발생하므로 github으로 설치

```
pip install -e git+https://github.com/mariocesar/sorl-thumbnail.git#egg=sorl-thumbnail
```

## settings.py 수정

```
INSTALLED_APPS = [
    # ...
    'sorl.thumbnail',
]
```

## 모델 변경

- 결국 thubnail_image 필드 제거
- 소소한 수정
```
class Photo(models.Model):
    image = models.ImageField(upload_to=user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return '{} {} {}'.format(self.owner.username, self.comment, self.is_public)
```

- migration도 잊지 말자.

```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

## 뷰 변경

- login_required를 잊지 말 것
- 간단하게 GET만 처리하므로 그냥 function view 사용
- urls.py 에서 넘어오는 pk가 parameter로 들어감을 기억할 것

```
@login_required
def profile(request, pk):
    user = get_object_or_404(User, pk=pk)
    # get 20 public photo only
    photos = user.photo_set.filter(is_public=True)[:20]
    context = {"profile_user": user, "photos": photos}
    return render(request, 'kilogram/profile.html', context)

```

## kilogram/urls.py 수정

- 기존의 CBV를 방금 만든 따끈한 function view로 교체

```
url(r'^profile/(?P<pk>[0-9]+)/$', views.profile, name='profile'),

```

## templates/kilogram/template 수정

- :exclamation: 상단에 `{% load thumbnail %} 추가
- profile 하단에 thumbnail을 추가
- 클릭하면 원본 이미지가 보이도록 하는 것도 어렵지 않음 (도전해 봅시다.)
- vue.js 등을 사용해서 single page app 으로 보이게 하는 것도?

```
{% load thumbnail %}

<div class="row">
    <div class="col-xs-6 col-md-3">
        {% if profile_user.profile.profile_photo %}
        <img class="round" src="{{profile_user.profile.profile_photo.url}}" width="200"> <br>
        {% else %}
        <img class="round" src="{% static 'kilogram/images/photo.jpg' %}" width="200"> <br>
        {% endif %}
    </div>

    <div class="col-xs-6 col-md-3">
        {% if profile_user.profile.nickname %}
        <h2>{{profile_user.profile.nickname}}</h2>
        {% endif %}
        {% if user == profile_user %}
        <a href="{% url 'kilogram:profile_update' %}">
            <button type="button" class="btn btn-default">프로필 편집</button></a></h2>
        {% endif %}
        <h3> username: {{profile_user.username}} <br>
            {% if profile_user.first_name is not None %}
            name: {{profile_user.first_name}} {{profile_user.last_name}} <br>
            {% endif %}
        </h3>
    </div>
</div> <!-- end row -->
<p> </p>
<div class="row">
    {%for photo in photos %}
    <div class="col-xs-6 col-md-4">
        {% thumbnail photo.image "300x300" crop="center" as im %}
        <img src="{{ im.url }}" width="{{ im.width }}" height="{{ im.height }}">
        {% endthumbnail %}
    </div>
    {% endfor %}
</div>
```
