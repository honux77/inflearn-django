# Class-based View

## function based view 와의 차이점
- GET, POST 와 같은 HTTP 메소드를 별도의 파이썬 메소드로 처리
- 객체 지향의 장점을 적용 가능 -재사용성, Mixin 등
- 복잡한 구현을 가능하게 해줌

---
# Generic views

- 웹 개발시 자주 사용하는 기능을 장고에서 미리 제공해 줌
- 코드의 단순화, 빠른 개발을 가능하게 함
- 투표 앱의 index() - 객체 전체 리스트를 화면에 표시 
- results(), detail() - 한 객체의 세부 정보를 화면에 표시

---
# generic view 적용하기
- polls/ulrs.py 수정
```python
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
```
- 주의사항: generic view를 위해서는 매개변수 이름이 pk여야 합니다.

---
- views.py 수정
```python
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
```
