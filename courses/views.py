# Django
from django.shortcuts import render
from django.views.generic import ListView, DetailView

# Djangorestframework
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

# Models
from .models import Course
from lessons.models import Lesson
from questions.models import Question

# Serializers
from .serializers import CourseSerializer, CreateCourseSerializer
from lessons.serializers import LessonSerializer


# Frontend Logic

def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'courses/courses.html', context)


# Course list view
class CourseListView(ListView):
    model = Course
    template_name = 'courses/courses.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'courses'
    ordering = ['id']
    paginate_by = 10


# Course detail view
class CourseDetailView(DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Call the base implementation first to get a context
        context['lessons'] = Lesson.objects.filter(course=self.object)  # Add in a QuerySet of all the commits
        return context


# Lesson detail view
class LessonDetailView(DetailView):
    model = Lesson

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # Call the base implementation first to get a context
        context['questions'] = Question.objects.filter(lesson=self.object)  # Add in a QuerySet of all the commits
        return context


# API courses endpoint logic
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
