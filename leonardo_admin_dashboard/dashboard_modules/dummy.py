# encoding: utf-8

from jet.dashboard.modules import DashboardModule
from django.utils.translation import ugettext_lazy as _


class DummyChartWidget(DashboardModule):
    module = None
    title = _('Visitors totals chart (dummy)')

    template = 'dashboard/modules/dummy_visitors_chart.html'


class DummyVisitorsWidget(DashboardModule):
    module = None
    title = _('Visitors totals (dummy)')
    template = 'dashboard/modules/dummy_visitors.html'


class DummyOnlineWidget(DashboardModule):
    module = None
    title = _('Visitors totals count (dummy)')
    template = 'dashboard/modules/dummy_visitors_count.html'
