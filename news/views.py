from django.shortcuts import render, get_object_or_404
from news.models import News


# Create your views here.

def news_list(request):
    """вывод всех новостей"""
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news":news})

def new_single(request, pk):
    """вывод полной статьи"""
    new = get_object_or_404(News, id=pk)
    return render(request, "news/new_single.html", {"new": new})
