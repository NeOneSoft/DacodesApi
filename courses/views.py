# Djangorestframework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from .models import Course
from lessons.models import Lesson

# Serializers
from .serializers import CourseSerializer, CreateCourseSerializer
from lessons.serializers import LessonSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateCourseSerializer
        return CourseSerializer

    # Additional Courses API service
    @action(detail=True, methods=['GET'])
    def lessons(self, request, pk=None):
        course = self.get_object()
        lessons = Lesson.objects.filter(course=course.id)
        serialized = LessonSerializer(lessons, many=True)
        if not lessons:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This course has not lessons'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
