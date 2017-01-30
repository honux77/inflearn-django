# 테스트 자동화하기

## 버그 확인
```shell
$ python manage.py shell 
>>> import datetime
>>> from django.utils import timezone
>>> from polls.models import Question
>>> future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=7))
>>> future_question.was_published_recently()
True
```

## 테스트 파일 작성
- polls/tests.py 수정
```
import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Question


class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

## 테스트 실행 
```
$ python manage.py test polls
```

## 버그 수정
- polls/models.py 수정
```
def was_published_recently(self):
    now = timezone.now()
    return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

## 더 많은 테스트 코드
```
def test_was_published_recently_with_old_question(self):
    """
    was_published_recently() should return False for questions whose
    pub_date is older than 1 day.
    """
    time = timezone.now() - datetime.timedelta(days=30)
    old_question = Question(pub_date=time)
    self.assertIs(old_question.was_published_recently(), False)

def test_was_published_recently_with_recent_question(self):
    """
    was_published_recently() should return True for questions whose
    pub_date is within the last day.
    """
    time = timezone.now() - datetime.timedelta(hours=1)
    recent_question = Question(pub_date=time)
    self.assertIs(recent_question.was_published_recently(), True)
```