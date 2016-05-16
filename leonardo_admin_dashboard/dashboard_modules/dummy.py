
from jet.dashboard.modules import DashboardModule
from django.utils.translation import ugettext_lazy as _


class DummyChartWidget(DashboardModule):
    module = None
    title = _('Dummy visitors chart')

    template = 'dashboard/modules/dummy_visitors_chart.html'


class DummyVisitorsWidget(DashboardModule):
    module = None
    title = _('Dummy Analytics visitors')
    template = 'dashboard/modules/dummy_visitors.html'


class DummyOnlineWidget(DashboardModule):
    module = None
    title = _('Dummy Analytics Online')
    template = 'dashboard/modules/dummy_visitors_count.html'
