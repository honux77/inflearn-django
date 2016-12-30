from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    q = get_object_or_404(Question, pk = question_id)
    return render(request, 'polls/detail.html', {'question': q})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def main(request):
    return HttpResponse("<h1>Hello, CodeSquad</h1>")
