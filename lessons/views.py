# Djangorestframework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from .models import Lesson
from questions.models import Question

# Serializers
from .serializers import LessonSerializer, CreateLessonSerializer
from questions.serializers import QuestionSerializer


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLessonSerializer
        return LessonSerializer

    # Additional Courses API service
    @action(detail=True, methods=['GET'])
    def questions(self, request, pk=None):
        lesson = self.get_object()
        questions = Question.objects.filter(lesson=lesson.id)
        serialized = QuestionSerializer(questions, many=True)
        if not questions:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This lesson has not questions'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
