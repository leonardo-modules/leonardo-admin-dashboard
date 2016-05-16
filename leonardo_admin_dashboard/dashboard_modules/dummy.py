
from jet.dashboard.modules import DashboardModule


class DummyChartWidget(DashboardModule):
    module = None
    title = u'Počet zákazníků za 24h'

    template = 'dashboard/modules/dummy_visitors_chart.html'


class DummyVisitorsWidget(DashboardModule):
    module = None
    title = u'Počet zákazníků'
    template = 'dashboard/modules/dummy_visitors.html'


class DummyOnlineWidget(DashboardModule):
    module = None
    title = 'Počet zákazníků online'
    template = 'dashboard/modules/dummy_visitors_count.html'
