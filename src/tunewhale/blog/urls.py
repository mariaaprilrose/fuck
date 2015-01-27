from django.conf.urls import patterns, url
from blog import views

urlpatterns = patterns('',
    url(r'^blog/$', views.index, name='index'),
    url(r'^blog/new/$', views.new_blog, name='new'),
    url(r'^blog/(?P<post_title>\w+)/$', views.post, name='post'),
)