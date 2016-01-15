
from django.conf.urls import include, patterns, url

urlpatterns = patterns('',
                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^jet/dashboard/',
                           include('jet.dashboard.urls', 'jet-dashboard')),
                       )
