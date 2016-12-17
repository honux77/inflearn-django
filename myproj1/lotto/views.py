from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.filter(update_date__lte=timezone.now()).order_by('-update_date')
    return render(request, 'lotto/lotto_view.html', {'posts': posts})

def detail(request, pk):    
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lotto/detail.html', {'post': post})
