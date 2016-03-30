from django.conf.urls import patterns, include, url
from .views import *




urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^contribution/create/$', ContributionCreateView.as_view(), name='contribution_create'),
    url(r'^pledge/create/$', PledgeCreateView.as_view(), name='pledge_create'),
)