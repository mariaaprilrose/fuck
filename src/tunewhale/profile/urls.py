from django.conf.urls import patterns, url
from profile import views

urlpatterns = patterns('',
    url(r'^(?P<user_username>\w+)/$', views.index, name='index'),
    url(r'^follow/(?P<user_to_follow>\w+)/$', views.follow, name='follow'),
    url(r'^unfollow/(?P<user_to_unfollow>\w+)/$', views.unfollow, name='unfollow'),
)