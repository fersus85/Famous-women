from django import template
from django.db.models import Count
from django.http import request
from django.contrib.sessions.models import Session
from women.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):

    cats = Category.objects.annotate(Count('women'))

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/main_menu.html')
def show_menu(cat_selected=0):

    menu = [{'title': 'About site', 'url_name': 'about'},
            {'title': 'Add article', 'url_name': 'add_page'},
            {'title': 'Callback', 'url_name': 'contact'},
            ]

    return {'menu': menu, 'cat_selected': cat_selected}


@register.inclusion_tag('women/main_menu2.html')
def show_menu2(cat_selected=0):

    menu = [{'title': 'About site', 'url_name': 'about'},
             {'title': 'Callback', 'url_name': 'contact'},
             ]
    return {'menu': menu, 'cat_selected': cat_selected}
