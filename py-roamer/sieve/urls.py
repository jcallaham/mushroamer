from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^encyclopedia/$', views.IndexView.as_view(), name='index'),                     # Home index of all Lactarius species in database
    url(r'^encyclopedia/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),    # Detail view of a particular species
    url(r'^sieve/$', views.query, name='query'),
]
