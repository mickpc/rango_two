from django.conf.urls import patterns, url
from rp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='home'))
