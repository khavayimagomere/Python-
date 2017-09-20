from django.conf.urls import url,include
from django.contrib import admin
from forumapp import views
from rest_framework import routers
from forumapp.views import StudentViewSet

router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^$', views.welcome),
    url(r'^students/$', views.students, name = 'students'),
]
