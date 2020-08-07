# Djangorestframework
from rest_framework import serializers

# Models
from .models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Lesson general purpose serializer
    """

    class Meta:
        model = Lesson
        fields = ('lesson', 'course_lesson', 'target_score')


class CreateLessonSerializer(serializers.ModelSerializer):
    """
    Create Lesson serializer
    """

    class Meta:
        model = Lesson
        fields = ('lesson', 'course_lesson', 'target_score')
