from django.shortcuts import render, redirect
from mainboard.forms import *

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else :
        form = Form()


    return render(request, 'write.html', {'form': form})

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})


def view(request, num ="1"):
    article = Article.objects.get(id=num)
    return render(request, 'view.html', {'article':article})


def comment(request, num="1"):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Article.objects.get(id=num)
            comment.save()
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form':form})






