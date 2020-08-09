# Django
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

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
from users.serializers import UserSerializer

# Frontend Logic


# Lesson detail view
class LessonDetailView(DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Call the base implementation first to get a context
        context['questions'] = Question.objects.filter(lesson=self.object)  # Add in a QuerySet of all the questions
        return context


# API lessons endpoint logic
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateLessonSerializer
        return LessonSerializer

    # Additional Courses API service
    # GET lessons questions
    @action(detail=True, methods=['GET'])
    def questions(self, request, pk=None):
        lesson = self.get_object()
        questions = Question.objects.filter(lesson=lesson.id)
        serialized = QuestionSerializer(questions, many=True)
        if not questions:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This lesson has not questions'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    # GET lessons students
    @action(detail=True, methods=['GET'])
    def students(self, request, pk=None):
        course = self.get_object()
        students = User.objects.filter(course=course.id)
        serialized = UserSerializer(students, many=True)
        if not students:
            return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'This lesson has not students'})
        return Response(status=status.HTTP_200_OK, data=serialized.data)
