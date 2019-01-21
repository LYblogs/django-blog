from django.shortcuts import render

from blog_back.models import Article


def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()[::-1]
        user = request.user
        
        return render(request, 'web_before/index.html', {'articles': articles}, {'user': user})


def about(request):
    return render(request, 'web_before/about.html')


def time(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        return render(request, 'web_before/time.html', {'articles': articles})


def info(request, id):
    if request.method == 'GET':
        art = Article.objects.filter(pk=id).first()
        return render(request, 'web_before/info.html', {'art': art})
