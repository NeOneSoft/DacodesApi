#Django
from django.conf.urls import url, include

#Djangorestframework
from rest_framework import routers

#Views
from courses.views import CourseViewSet
from lessons.views import LessonViewSet

#API urls
router = routers.DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]