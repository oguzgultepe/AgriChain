from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submitbatch/(?P<pk>[0-9]+)/$', views.submit, name='submit'),
]
