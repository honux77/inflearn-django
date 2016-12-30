# App2
## 2-1 준비 
0. virtualenv 활성화
1. 프로젝트 생성
$ django-admin startproject mysite

2. 서버 시작 및 settings.py 수정
$ python manage.py runserver
$ python manage.py ryunserver 8080

3. 앱 생성 
$ python manage.py startapp polls

4. 첫번째 뷰 
- views.py 수정 
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

5. polls/urls.py 생성 (new!)
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

6. mysite/urls.py 수정 (new!)
    url(r'^polls/', include('polls.urls')),

7. app 등록
- settings.py 수정: polls app 등록 

$ python manage.py migrate

# 2-2 Model 

ORM이란? Object Relational Mapping 

8. models.py 수정

Model 변경의 3단계: models.py 수정 - makemigrations - migrate  

- polls/models.py

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

$ python manage.py makemigrations polls
$ python manage.py sqlmigrate polls 0001
$ python manage.py migrate


9. django shell 1

$ python manage.py shell
>>> from polls.models import Question, Choice
>>> Question.objects.all()
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()

10. models.py 수정

from django.utils import timezone
import datetime

class Question(models.Model):
    # ...
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    # ...
    def __str__(self):
        return self.choice_text

11. django shell 2

>>> from polls.models import Question, Choice
>>> Question.objects.all()
>>> Question.objects.filter(id=1)
>>> Question.objects.filter(question_text__startswith='What')
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
>>> Question.objects.get(id=2)
>>> Question.objects.get(pk=1)
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()

12. django shell 3

>>> q.choice_set.all()
>>> q.choice_set.create(choice_text='Not much', votes=0)
>>> q.choice_set.create(choice_text='The sky', votes=0)
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)
>>> c.question

>>> q.choice_set.all()
>>> q.choice_set.count()
>>> Choice.objects.filter(question__pub_date__year=current_year)

>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()

13. admin 페이지 사용하기 

$ python manage.py createsuperuser

- admins.py 수정 

from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

# 2-3 

14. views.py 수정 

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

15. urls.py 수정 

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

16. views.py 수정

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)

17. template 만들기

- polls/template/polls/index.html 

{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}

18. views.index 수정

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

19. 404 처리하기 

- polls/detail.html 생성

{{ question }}

- views.py 수정 

from django.http import Http404
from .models import Question

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

20. 404 shortcut 
from django.shortcuts import get_object_or_404, render
from .models import Question

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

21. 하드코딩 url 수정하기 
- urls.py 수정

from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

- index.html 수정
<!-- <a href="/polls/{{ question.id }}/"> -->
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>

# 2-4 

22. template에 폼 추가 
- detail.html 수정

<h1>{{ question.question_text }}</h1>

{% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}

<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
{% for choice in question.choice_set.all %}
    <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}" />
    <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br />
{% endfor %}
<input type="submit" value="Vote" />
</form>
