from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required



urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/register/$', UserProfileRegistrationView.as_view(), name='registration_register'),                   
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^contribution/create/$', login_required(ContributionCreateView.as_view()), name='contribution_create'),
    url(r'^pledge/create/$', login_required(PledgeCreateView.as_view()), name='pledge_create'),
    url(r'^contribution/$', login_required(ContributionListView.as_view()), name='contribution_list'),
    url(r'^pledge/$', login_required(PledgeListView.as_view()), name='pledge_list'),
    url(r'^contribution/(?P<pk>\d+)/$', login_required(ContributionDetailView.as_view()), name='contribution_detail'),
    url(r'^pledge/(?P<pk>\d+)/$', login_required(PledgeDetailView.as_view()), name='pledge_detail'),
    url(r'^contribution/update/(?P<pk>\d+)/$', login_required(ContributionUpdateView.as_view()), name='contribution_update'),
    url(r'^pledge/update/(?P<pk>\d+)/$', login_required(PledgeUpdateView.as_view()), name='pledge_update'),
    url(r'^contribution/delete/(?P<pk>\d+)/$', login_required(ContributionDeleteView.as_view()), name='contribution_delete'),
    url(r'^pledge/delete/(?P<pk>\d+)/$', login_required(PledgeDeleteView.as_view()), name='pledge_delete'),
    url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
    url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
    url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
    url(r'^about_us/', AboutUsView.as_view(), name='about_us'),
    url(r'^search/$', login_required(SearchContributionListView.as_view()), name='search'),
    url(r'^parent_tips/', ParentTipsView.as_view(), name='parent_tips'),
    url(r'^leaderboards/', UserListView.as_view(), name='leaderboards'),
)