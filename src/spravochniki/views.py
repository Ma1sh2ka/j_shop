from django.shortcuts import render

from . import models

# Create your views here.

def author(request, author_id):
    author = models.Author.objects.get(pk=author_id)
    ctx = {
        'author': author,
    }
    return render(request, template_name='author_detail.html', context=ctx)

def author_list(request):
    author_list = models.Author.objects.all()
    ctx = {
        'author_list': author_list,
    }
    return render(request, template_name='author_list.html', context=ctx)


def series(request, series_id):
    series = models.Series.objects.get(pk=series_id)
    ctx = {
        'series': series,
    }
    return render(request, template_name='series_detail.html', context=ctx)

def series_list(request):
    series_list = models.Series.objects.all()
    ctx = {
        'series_list': series_list,
    }
    return render(request, template_name='series_list.html', context=ctx)


def genre(request, genre_id):
    genre = models.Genre.objects.get(pk=genre_id)
    ctx = {
        'genre': genre,
    }
    return render(request, template_name='genre_detail.html', context=ctx)

def genre_list(request):
    genre_list = models.Genre.objects.all()
    ctx = {
        'genre_list': genre_list,
    }
    return render(request, template_name='genre_list.html', context=ctx)

def publishing_house(request, publishing_house_id):
    publishing_house = models.Publishing_house.objects.get(pk=publishing_house_id)
    ctx = {
        'publishing_house': publishing_house,
    }
    return render(request, template_name='publishing_house_detail.html', context=ctx)

def publishing_house_list(request):
    publishing_house_list = models.Publishing_house.objects.all()
    ctx = {
        'publishing_house_list': publishing_house_list,
    }
    return render(request, template_name='publishing_house_list.html', context=ctx)

def home(request):
    return render(request, template_name='homepage.html', context={})