from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.lists, name = 'lists'),
    url(r'^$', views.create, name = 'create'),
    url(r'^$', views.details, name = 'details'),
    ]
