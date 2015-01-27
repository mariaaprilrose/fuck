from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('authactions.urls', namespace='auth')),
    url(r'^', include('blog.urls', namespace='blog')),
    url(r'^', include('profile.urls', namespace='profile')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.contrib.staticfiles.views',
                            url(r'^static/(?P<path>.*)$', 'serve'),)