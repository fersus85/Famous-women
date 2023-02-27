from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render
from .models import *


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Main page',
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'title': 'About site'})


def addpage(request):
    return HttpResponse('add article')


def contact(request):
    return HttpResponse('contacts')


def login(request):
    return HttpResponse('authorization')


def show_post(request, post_id):
    return HttpResponse(f'display article id = {post_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Categories'
    }
    return render(request, 'women/index.html', context=context)
