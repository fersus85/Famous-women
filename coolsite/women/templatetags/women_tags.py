from django import template
from women.models import *


register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('women/main_menu.html')
def show_menu(cat_selected=0):
    menu = [{'title': 'About site', 'url_name': 'about'},
            {'title': 'Add article', 'url_name': 'add_page'},
            {'title': 'Callback', 'url_name': 'contact'},
            {'title': 'Enter', 'url_name': 'login'}
            ]
    return {'menu': menu, 'cat_selected': cat_selected}
