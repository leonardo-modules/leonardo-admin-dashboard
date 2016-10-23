
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from importlib import import_module
from leonardo import leonardo
from . import modules

MENU = [
    modules.MenuModelList(
        _('Web content'),
        models=('web.*', 'sites.*', 'media.*', "leonardo_module_links.*",),
        exclude=('web.WidgetDimension', 'web.PageColorScheme',
                 "leonardo_module_links.Link",
                 'web.PageDimension', 'media.Clipboard',
                 'media.Document', 'media.Image', "media.FolderPermission",
                 "media.File",
                 "media.FolderTranslation",
                 "media.Vector",
                 "media.Video",
                 "media.Flash",
                 "media.ImageTranslation", "web.WidgetContentTheme",
                 "web.WidgetBaseTheme",
                 "web.PageDimension",
                 "web.PageTheme",),
        column=2,
        order=0
    )
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
