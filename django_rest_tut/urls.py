from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# default login/logout/views
urlpatterns = patterns(
    '',
    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),
    url(r'^quickstart/', include('quickstart.urls')),
    url(r'^$', 'snippets.views.api_root'),
    url(r'^', include('snippets.urls')),

)
    # Examples:
    # url(r'^$', 'django_rest_tut.views.home', name='home'),
    # url(r'^django_rest_tut/', include('django_rest_tut.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
