
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from jet.dashboard.modules import AppList, LinkList, ModelList
from jet.utils import get_app_list


class RenderMixin(object):

    # change if you want show module title
    show_title = False

    def render_submenu(self, request=None):
        '''render submenu if footer flag is specified'''
        if request:
            self.context['request'] = request

        if hasattr(self, 'footer'):
            self.init_with_context(self.context)
            return render_to_string(self.template_footer,
                                    self.get_context_data())
        return ''

    def render(self, request=None):
        if request:
            self.context['request'] = request
        return super(RenderMixin, self).render()


class MenuLinkList(RenderMixin, LinkList):
    """
    List of links widget.
    Usage example:
    .. code-block:: python
        from django.utils.translation import ugettext_lazy as _
        from jet.dashboard import modules
        from jet.dashboard.dashboard import Dashboard, AppIndexDashboard
        class CustomIndexDashboard(Dashboard):
            columns = 3
            def init_with_context(self, context):
                self.available_children.append(modules.LinkList)
                self.children.append(modules.LinkList(
                    _('Support'),
                    children=[
                        {
                            'title': _('Django documentation'),
                            'url': 'http://docs.djangoproject.com/',
                            'external': True,
                        },
                        {
                            'title': _('Django "django-users" mailing list'),
                            'url': 'http://groups.google.com/group/django-users',
                            'external': True,
                        },
                        {
                            'title': _('Django irc channel'),
                            'url': 'irc://irc.freenode.net/django',
                            'external': True,
                        },
                    ],
                    column=0,
                    order=0
                ))
    """

    title = _('Menu Links')
    template = 'dashboard/modules/menu_link_list.html'

    #: Specify widget layout.
    #: Allowed values ``stacked`` and ``inline``.
    layout = 'stacked'

    children = []
    child_name = _('Link')
    child_name_plural = _('Links')

    def parse_link(self, link):
        '''Support icon as string'''
        if isinstance(link, (tuple, list)):
            link_dict = {'title': link[0], 'url': link[1]}

            if len(link) >= 3:
                for l in link[2:]:
                    if isinstance(l, bool):
                        link_dict['external'] = l
                    else:
                        link_dict['icon'] = l

            return link_dict
        elif isinstance(link, (dict,)):
            return link


class SubMenuLinkList(MenuLinkList):
    '''Just shows childrens in submenu'''
    footer = True
    template = 'dashboard/modules/submenu_link_list.html'
    template_footer = 'dashboard/modules/_submenu_link_list.html'


class MenuAppList(RenderMixin, AppList):
    template = 'dashboard/modules/menu_app_list.html'
    template_footer = 'dashboard/modules/_submenu_app_list.html'
    footer = True

    def get_exclude(self):
        if self.exclude:
            return [e.lower() for e in self.exclude]
        return []

#    def init_with_context(self, context):
#        app_list = get_app_list(context)
#        app_to_remove = []
#
#        for app in app_list:
#            app['models'] = filter(
#                lambda model: self.models is None or model['object_name'] in self.models or app.get(
#                    'app_label', app.get('name')) + '.*' in self.models,
#                app['models']
#            )
#
#            # really hell
#            app['models'] = filter(
#                lambda model: (model['object_name'].lower() not in self.get_exclude() and (app.get(
#                    'app_label', app.get('name')) + '.*') not in self.get_exclude() and (app.get(
#                    'app_label', app.get('name')) + '.' + model['object_name'].lower()) not in self.get_exclude()),
#                app['models']
#            )
#            app['models'] = list(app['models'])
#
#            if self.hide_empty and len(list(app['models'])) == 0:
#                app_to_remove.append(app)
#
#        for app in app_to_remove:
#            app_list.remove(app)
#
#        self.children = app_list


class MenuModelList(RenderMixin, ModelList):
    footer = True
    template = 'dashboard/modules/menu_model_list.html'
    template_footer = 'dashboard/modules/_menu_model_list.html'

    def __init__(self, *args, **kw):
        self.index_url = kw.pop('index_url', '')
        super(MenuModelList, self).__init__(*args, **kw)
