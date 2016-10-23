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


@register.assignment_tag
def filter_fieldsets_with_errors(fieldsets):
    i = 0
    fieldsets_with_errors = list()

    for fieldset in fieldsets:
        errors = False

        for line in fieldset:
            for field in line:
                if hasattr(field.field, 'errors') and len(field.field.errors) > 0:
                    errors = True
                    break
            if errors:
                break

        if errors:
            fieldsets_with_errors.append(i)

        i += 1

    return fieldsets_with_errors


@register.assignment_tag
def is_fieldset_selected(fieldset_index, fieldsets_with_errors):
    if len(fieldsets_with_errors) == 0:
        return fieldset_index == 0
    else:
        return fieldset_index == fieldsets_with_errors[0]


@register.assignment_tag
def is_fieldset_with_errors(fieldset_index, fieldsets_with_errors):
    return fieldset_index in fieldsets_with_errors


@register.assignment_tag
def formset_has_errors(formset):
    if formset is None or getattr(formset, 'errors') is None:
        return False
    for errors in formset.errors:
        if errors:
            return True
    return False
