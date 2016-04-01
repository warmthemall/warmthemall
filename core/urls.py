from django.conf.urls import patterns, include, url
from .views import *




urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^contribution/create/$', ContributionCreateView.as_view(), name='contribution_create'),
    url(r'^pledge/create/$', PledgeCreateView.as_view(), name='pledge_create'),
    url(r'^contribution/$', ContributionListView.as_view(), name='contribution_list'),
    url(r'^pledge/$', PledgeListView.as_view(), name='pledge_list'),
    url(r'^contribution/(?P<pk>\d+)/$', ContributionDetailView.as_view(), name='contribution_detail'),
    url(r'^pledge/(?P<pk>\d+)/$', PledgeDetailView.as_view(), name='pledge_detail'),
    url(r'^contribution/update/(?P<pk>\d+)/$', ContributionUpdateView.as_view(), name='contribution_update'),
    url(r'^pledge/update/(?P<pk>\d+)/$', PledgeUpdateView.as_view(), name='pledge_update'),
)