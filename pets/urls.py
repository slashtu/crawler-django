from django.conf.urls import patterns, url

from pets import views

urlpatterns = patterns('',
        #index
        url(r'^$', views.index, name='index'),
)