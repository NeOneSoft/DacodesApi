# Django
from django.urls import path

# Views
from .views import CourseListView, CourseDetailView, LessonDetailView

# Frontend urls
urlpatterns = [
    path('', CourseListView.as_view(), name='courses'),
    path('course/<int:pk>/', CourseDetailView.as_view(), name='courses-detail'),
    path('course/<int:pk>/questions', LessonDetailView.as_view(), name='lessons-detail')
]
