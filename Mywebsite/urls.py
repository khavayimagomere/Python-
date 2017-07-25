from django.conf.urls import url
from .import views

urlpatterns = [
    url('r^$', views.list, name ='list'),
    url('r^$', views.details, name ='details'),
    url('r^$', views.update, name ='update'),
    
 ]