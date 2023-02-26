from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = ['about site', 'add article', 'callback', 'Enter']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})


def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by categories</h1><p>{cat}</p>')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
