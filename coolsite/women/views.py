from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

menu = [{'title': 'About site', 'url_name': 'about'},
        {'title': 'Add article', 'url_name': 'add_page'},
        {'title': 'Callback', 'url_name': 'contact'},
        {'title': 'Enter', 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page'
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About site'})


def addpage(request):
    return HttpResponse('add article')


def contact(request):
    return HttpResponse('contacts')


def login(request):
    return HttpResponse('authorization')


def show_post(request, post_id):
    return HttpResponse(f'display article id = {post_id}')
def categories(request, cat):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Articles by categories</h1><p>{cat}</p>')



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
