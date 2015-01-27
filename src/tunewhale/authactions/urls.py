from django.conf.urls import patterns, url
from authactions import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^home/$', views.home, name='home'),
    url(r'^contact/$', views.contact_view, name='contact'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^signup/$', views.signup_view, name='signup'),
    url(r'^\w$', views.page404)
)