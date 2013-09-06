from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
    # from django.contrib import admin
    # admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'dashboard.views.home', name='home'),
                       url(r'^reports/', include('reports.urls')),
                       url(r'^documents/', include('documents.urls')),
                       url(r'^orders/', include('orders.urls')),
                       url(r'^search/', include('search.urls')),
                       url(r'^parts/', include('parts.urls')),
                       url(r'^vendors/', include('vendors.urls')),

                       url('^accounts/', include('django.contrib.auth.urls')),
                       url('^activity/', include('actstream.urls')),

                       # Admin related urls
                       (r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^djangojs/', include('djangojs.urls')),
                      )
