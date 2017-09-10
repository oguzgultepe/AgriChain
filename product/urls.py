from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit/(?P<pk>[0-9]+)/$', views.submit, name='submit'),
    url(r'^batch/(?P<pk>.*)/$', views.batch, name='batch'),
    url(r'^client/(?P<pk>.*)/$', views.client, name='client'),
]
