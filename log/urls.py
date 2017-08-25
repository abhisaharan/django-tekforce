#!python
# log/urls.py
from django.conf.urls import url
from . import views


# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^stocks/$', views.stocks, name='stocks'),
    url(r'^home/$', views.home, name='home'),
]
