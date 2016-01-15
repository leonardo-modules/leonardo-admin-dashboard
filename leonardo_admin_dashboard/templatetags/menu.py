from django import template
from ..menu import MENU
register = template.Library()


@register.assignment_tag
def get_sidebar_menu():
    return MENU


@register.filter
def render_module(module, request):
    return module.render(request)


@register.filter
def render_submenu(module, request):
    return module.render_submenu(request)
