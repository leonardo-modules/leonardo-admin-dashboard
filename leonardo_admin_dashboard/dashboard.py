# encoding: utf-8
from django.utils.translation import ugettext_lazy as _
from jet.dashboard.dashboard import AppIndexDashboard, Dashboard

from . import modules
from leonardo import leonardo
from importlib import import_module


class CustomIndexDashboard(Dashboard):

    '''Default Leonardo Dashboard with some generic stuff
    '''

    columns = 3

    def register_widgets(self):
        '''Iterate over optional dashboard_widgets
        and append all to main dashboard
        '''
        for widget in getattr(leonardo.config,
                              'dashboard_widgets', []):
            try:
                module = '.'.join(widget.split('.')[:-1])
                name = widget.split('.')[-1]
                instance = getattr(import_module(module), name)
                self.children.append(instance)
            except ImportError:
                raise Exception('Widget cannot be registred %s' % widget)

    def register_available_widgets(self):
        '''Iterate over optional widgets and regiter all'''

        for widget in getattr(leonardo.config,
                              'dashboard_widgets_available', []):
            try:
                module = '.'.join(widget.split('.')[:-1])
                name = widget.split('.')[-1]
                instance = getattr(import_module(module), name)
                self.available_children.append(instance)
            except ImportError:
                raise Exception('Widget cannot be registred %s' % widget)

    def register_optional_ga(self):
        '''Optionaly register Google Analytics'''

        try:
            from .dashboard_modules import google_analytics
            self.available_children.append(
                google_analytics.GoogleAnalyticsVisitorsTotals)
            self.available_children.append(
                google_analytics.GoogleAnalyticsVisitorsChart)
            self.available_children.append(
                google_analytics.GoogleAnalyticsPeriodVisitors)
        except:
            pass

    def register_dummy(self):
        '''Optionaly register Google Analytics'''

        try:
            from .dashboard_modules import dummy
            self.available_children.append(
                dummy.DummyChartWidget)
            self.available_children.append(
                dummy.DummyVisitorsWidget)
            self.available_children.append(
                dummy.DummyOnlineWidget)
        except:
            pass


    def init_with_context(self, context):

        # register some defaults
        self.available_children.append(modules.LinkList)
        self.available_children.append(modules.Feed)

        # optionaly register GA
        self.register_optional_ga()

        # register dummy graphs
        self.register_dummy()

        # register custom widgets
        self.register_available_widgets()
        self.register_widgets()

        # append a link list module for "quick links"
        self.children.append(modules.LinkList(
            _('Quick Actions'),
            layout='inline',
            draggable=False,
            deletable=False,
            collapsible=False,
            children=[
                [_('Return to site'), '/'],
            ],
            column=0,
            order=0
        ))

        # append a recent actions module
        self.children.append(modules.RecentActions(
            _('Recent Actions'),
            10,
            column=0,
            order=1
        ))

        # append a feed module
        self.children.append(modules.Feed(
            _('Latest Leonardo News'),
            feed_url='https://www.leonardo-cms.org/en/news/feed/',
            limit=5,
            column=1,
            order=1
        ))

        self.children.append(modules.LinkList(
            _('Support'),
            children=[
                {
                    'title': _('Leonardo CMS'),
                    'url': 'https://leonardo-cms.org',
                    'external': True,
                },
                {
                    'title': _('Leonardo documentation'),
                    'url': 'https://leonardo-cms.org/',
                    'external': True,
                },
                {
                    'title': _('Leonardo Packages'),
                    'url': 'https://packages.leonardo-cms.org',
                    'external': True,
                },
                {
                    'title': _('Report Bug or Request Feature'),
                    'url': 'https://github.com/django-leonardo/django-leonardo/issues',
                    'external': True,
                },
            ],
            column=2,
            order=1
        ))


class CustomAppIndexDashboard(AppIndexDashboard):

    def init_with_context(self, context):
        self.available_children.append(modules.LinkList)
        self.available_children.append(modules.Feed)

        self.children.append(modules.ModelList(
            title='Application models',
            models=self.models(),
            column=0,
            order=0
        ))
        self.children.append(modules.RecentActions(
            include_list=self.get_app_content_types(),
            column=1,
            order=0
        ))
