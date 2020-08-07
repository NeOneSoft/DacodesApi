#Django
from django.conf.urls import url, include

#Djangorestframework
from rest_framework import routers

#Views
from courses.views import CourseViewSet

#API urls
router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]