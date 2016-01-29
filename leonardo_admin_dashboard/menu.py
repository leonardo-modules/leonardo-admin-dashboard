
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from importlib import import_module
from leonardo import leonardo
from . import modules

MENU = [
    modules.MenuLinkList(
        _('Quick links'),
        draggable=False,
        deletable=False,
        collapsible=False,
        post_content=True,
        children=[
            [_('Return to site'), '/', 'icon-open-external'],
            [_('Home'), reverse('admin:index'), 'icon-data'],
            [_('Documentation'), reverse('django-admindocs-docroot'),
             'icon-book'],
        ],
        column=0,
        order=0
    ),
    modules.MenuModelList(
        _('Web'),
        models=('web.*', 'sites.*'),
        exclude=('web.WidgetDimension', 'PageDimension',),
        index_url=lambda url=reverse('admin:index'): url + 'web/' if url.endswith('/') else url + '/web/',
        column=2,
        order=0
    ),
    modules.MenuModelList(
        _('Media'),
        models=('media.*',),
        index_url=lambda url=reverse('admin:index'): url + 'media/' if url.endswith('/') else url + '/media/',
        column=3,
        order=10
    ),
]

# this step requires adding dashboard_menu to LEONARDO_CONF_SPEC dictinary
# then iter over collected menus and include it into main menu
for item in getattr(leonardo.config, 'dashboard_menu', []):
    try:
        module = '.'.join(item.split('.')[:-1])
        obj = item.split('.')[-1]
        instance = getattr(import_module(module), obj)
        MENU.append(instance)
    except ImportError:
        pass
