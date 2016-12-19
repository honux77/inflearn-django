## 장고로 웹 개발하기 1-1

## 장고 MTV 그림 및 설명
Model: 데이터베이스에 데이터를 저장하기 위한 객체
Template: 장고에서 사용하는 html 파일 (모양자)
View: 보여줄 데이터를 선택하는 계층, url에 연결된 파이썬 콜백 함수
MVC와는 다르다.

## 프로젝트 및 앱 생성 hello-world

1. 프로젝트 생성
$ djangoadmin startproject myproj1

2. app 생성
$ python manage.py startapp lotto

3. setting 파일 수정 및 app 등록
timezone = ‘Asia/Seoul’
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
...
INSTALLED_APPS = [
     ... ,
    'lotto',
]

4. server start
$ python manage.py runserver

5. urls.py 수정
from .lotto import views
url(r'^hello/$', views.hello),

6. views.py
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello, CodeSquad</h1>")


## Model 생성

urls.py 추가 설명
admin  url 접속

1. 모델 생성.
http://pastebin.com/Kr0Yw8Dz
from django.db import models
from django.utils import timezone
import random

# Create your models here.
class GuessNumbers(models.Model):
    name = models.CharField(max_length=24)
    lottos = models.CharField(max_length=120)
    numbers = models.IntegerField()
    text = models.CharField(max_length=255)
    update_date = models.DateTimeField()

    def __genLotto(self):
        self.lottos = ""
        origin = list(range(1,46))
        for _ in range(0, self.numbers):
            random.shuffle(origin)
            guess = origin[0:6]
            guess.sort()
            self.lottos += str(guess) + "\n"

    def generate(self):
        self.__genLotto()
        self.update_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s %s (%s)" % (self.name, self.text, self.numbers)

    def __str__(self):
        return self.title + ": " + self.bonus

2. 데이터베이스 수정 (변경내용 확인)
$ python manage.py makemigrations
$ python manage.py migrate

3. amdin 모드 확인 및 superuser 생성
$ python manage.py createsuperuser //minami

4. admin.py에 모델 등록
from lotto.models import GuessNumbers
admin.site.register(GuessNumbers)

5. 사이트에서 확인 및 데이터 입력

6. 모델 클래스에 __str__ 구현 및 재확인

7. 요약 (model 만들기 및 admin을 이용한 데이터 입력)

## test 코드 작성하기
1. 설명
2. 코드
3. 테스트
from django.test import TestCase

# Create your tests here.
from lotto.models import GuessNumbers
from django.utils import timezone
class GuessNumbersTestCase(TestCase):
    def test_gen_lotto_works(self):
        n = GuessNumbers(name = "test", numbers = 1, update_date = timezone.now())
        n.generate() #internally it calls __genLotto()
        print(n.lottos)
        self.assertTrue(len(n.lottos.split()) == 6)
        n.delete()


## view 와 템플릿 연동

1. urls.py 수정
url(r'^$', views.index),

2. views 수정
def index(request):
    return render(request, "lotto/default.html", {})

3. template 만들기
lotto/templates/lotto.html
http://pastebin.com/ydGGnM4S

4. 정적 파일 연동
lotto/static/css/lotto.css
http://pastebin.com/67KJKNCk

lotto/templates/lotto.html
{% load staticfiles %} 추가
<link rel="stylesheet" href="{% static 'css/lotto.css' %}">

$ python manage.py collectstatic

## django shell을 이용한 데이터 조작

1. models generate 메소드 만들기

2. shell에서 QuerySet 테스트해보기
all(), get(), filter()

3. generate() 메소드 실행 및 결과 확인

## view와 model과 연동

1. urls.py 수정
url(r'^$', views.index, name = "lotto_main"),

2. views 수정
from lotto.models import GuessNumbers
def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, "lotto/default.html", {"lottos": lottos})

3. default.html 수정
<div class="container lotto">
  {% for lotto in lottos%}
  <h2>{{lotto.text}}</h2>
  <p> last update: {{lotto.update_date}} by {{lotto.name}}</p>
  <p> {{lotto.lottos|linebreaksbr }}</p>
  {% endfor %}
</div>

## Form 만들기
1. form.py 작성
from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text',)

2. urls.py 및 views.py 수정
url(r'^newlotto/$', views.post, name = "lotto_new"),

def post(request):
    form = PostForm()
    return render(request, "lotto/form.html",{"form": form})

3. lotto/form.html 작성
http://pastebin.com/T75xXWUn

4. views.py 수정
def post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit = False)
            lotto.generate()
            return redirect('lotto_main')
    else:
        form = PostForm()
        return render(request, "lotto/form.html",{"form": form})


## 다듬기
1. urls.py 추가
url(r'^lotto/(?P<pk>[0-9]+)/$', views.detail, name = "lotto_detail"),

2. views.py 수정
def detail(request, pk):
        lotto = GuessNumbers.objects.get(pk = pk)
        return render(request, "lotto/detail.html", {"lotto": lotto})

3. lotto_detail.html 작성
<div class="container lotto">
  <h2>{{lotto.text}}</h2>
  <p> last update: {{lotto.update_date}} by {{lotto.name}}</p>
  <p> {{lotto.lottos|linebreaksbr }}</p>
</div>

4. default.html 수정

<div class="page-header">
<h1>My Lotto Page
  <a href="{% url 'lotto_new' %}"<span class="glyphicon glyphicon-plus btn btn-default"></span></a></h1>
</div>

<h2><a href="{% url 'lotto_detail' pk=lotto.pk %}">{{lotto.text}}</a></h2>
