# App2 Tutorial 2
## app 등록
- settings.py 수정: polls app 등록
``` bash
$ python manage.py migrate
```

## Model과 ORM

- ORM이란? Object Relational Mapping

## models.py 수정

- Model 변경의 3단계: models.py 수정 - makemigrations - migrate  

- polls/models.py 수정
```python
class Question(models.Model):
   question_text = models.CharField(max_length=200)
   pub_date = models.DateTimeField('date published')


class Choice(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   choice_text = models.CharField(max_length=200)
   votes = models.IntegerField(default=0)
```
- Question - Choice에는 1:n의 관계가 성립합니다.
- 즉 하나의 질문에는 여러 선택지가 올 수 있고, 선택지는 반드시 하나의 질문에 속하는 관계
```bash
$ python manage.py makemigrations polls
$ python manage.py sqlmigrate polls 0001
$ python manage.py migrate
```

## django shell 1

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

## models.py 수정

```python
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
