from django.shortcuts import render
# Create your views here.
from django.shortcuts import redirect
from .models import GuessNumbers
from .form import PostForm

def index(request):
    lottos = GuessNumbers.objects.order_by('-update_date')
    return render(request, "lotto/default.html", {"lottos": lottos})

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

def detail(request, pk):
        lotto = GuessNumbers.objects.get(pk = pk)
        return render(request, "lotto/detail.html", {"lotto": lotto})
