from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from quickstart.views import UserList, UserDetail, GroupList, GroupDetail


urlpatterns = patterns(
    'quickstart.views',
    url(r'^$', 'api_root'),
    url(r'^users/$', UserList.as_view(), name='user-list'),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view(), name='user-detail'),
    url(r'^groups/$', GroupList.as_view(), name='group-list'),
    url(r'^groups/(?P<pk>\d+)/$', GroupDetail.as_view(), name='group-detail'),
)

# format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
