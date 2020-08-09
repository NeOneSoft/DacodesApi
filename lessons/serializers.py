# Djangorestframework
from rest_framework import serializers

# Models
from .models import Lesson

# Serializers
from courses.serializers import CourseSerializer



class LessonSerializer(serializers.ModelSerializer):
    """
    Lesson general purpose serializer
    """
    # Using serializers from Courses and Questions
    course = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = ('lesson', 'target_score', 'course', 'students')


class CreateLessonSerializer(serializers.ModelSerializer):
    """
    Create Lesson serializer
    """

    class Meta:
        model = Lesson
        fields = ('lesson', 'target_score', 'course', 'students')
