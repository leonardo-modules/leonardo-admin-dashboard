
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

default_app_config = 'leonardo_admin_dashboard.Config'

LEONARDO_ORDERING = -2

LEONARDO_APPS = ['leonardo_admin_dashboard', 'jet.dashboard', 'jet', ]

LEONARDO_CONFIG = {
    'ANALYTICS_OAUTH_CLIENT_ID': ('8082..', _(
        'OAuth Client ID')),
    'ANALYTICS_OAUTH_CLIENT_SECRET': ('secret', _(
        'OAuth Client Secret')),
}


class Config(AppConfig):
    name = 'leonardo_admin_dashboard'
    verbose_name = "leonardo-admin-dashboard"
