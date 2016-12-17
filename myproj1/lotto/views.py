from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
import logging

# Create your views here.
def index(request):
    posts = Post.objects.filter(update_date__lte=timezone.now()).order_by('-update_date')
    return render(request, 'lotto/lotto_view.html', {'posts': posts})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'lotto/detail.html', {'post': post})

def lotto_new(request):
    logger = logging.getLogger(__name__)

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():

            post = form.save(commit=False)
            if type(request.user) == User:
                post.author = request.user
            else:
                post.author = User.objects.get(username='john')
            post.publish()
            return redirect('lotto_detail', pk = post.pk)
    else:
        form = PostForm()
        return render(request, 'lotto/lotto_edit.html', {'form': form})
