# Djangorestframework
from rest_framework import serializers

# Models
from .models import Course


class CourseSerializer(serializers.ModelSerializer):
    """
    Course general purpose serializer
    """

    class Meta:
        model = Course
        fields = ['course', 'students']


class CreateCourseSerializer(serializers.ModelSerializer):
    """
    Create Course serializer
    """

    class Meta:
        model = Course
        fields = ['course', 'students']
