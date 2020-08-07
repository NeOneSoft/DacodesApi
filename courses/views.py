# Djangorestframework
from rest_framework import viewsets

# Models and Serializers
from .models import Course
from .serializers import CourseSerializer, CreateCourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCourseSerializer
        return CourseSerializer
