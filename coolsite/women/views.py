from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
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


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'title': post.title,
        'cat_selected': post.cat_id
    }
    return render(request, 'women/post.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')


def show_category(request, cat_slug):
    if cat_slug == 'singers':
        cat_id = 2
    else:
        cat_id = 1
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Categories'
    }
    return render(request, 'women/index.html', context=context)
