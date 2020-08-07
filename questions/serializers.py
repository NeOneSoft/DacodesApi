# Djangorestframework
from rest_framework import serializers

# Models
from .models import Question


class QuestionSerializer(serializers.ModelSerializer):
    """
    Question general purpose serializer
    """

    class Meta:
        model = Question
        fields = ('question', 'lesson_question', 'type_question', 'score')


class CreateQuestionSerializer(serializers.ModelSerializer):
    """
    Create Question serializer
    """

    class Meta:
        model = Question
        fields = ('question', 'lesson_question', 'type_question', 'score')