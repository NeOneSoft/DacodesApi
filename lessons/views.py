# Djangorestframework
from rest_framework import viewsets

# Models and Serializers
from .models import Lesson
from .serializers import LessonSerializer, CreateLessonSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLessonSerializer
        return LessonSerializer
