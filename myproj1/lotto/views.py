from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
def index(request):
    str = "<h1>Hello inflearn</h1><p>%s</p>" % datetime.now().isoformat()
    return HttpResponse(str)
