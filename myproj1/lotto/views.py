from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(update_date__lte=timezone.now()).order_by('-update_date')
    return render(request, 'lotto/lotto_view.html', {'posts': posts})
