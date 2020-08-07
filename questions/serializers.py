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
        fields = ('question', 'type_question', 'score', 'lesson')


class CreateQuestionSerializer(serializers.ModelSerializer):
    """
    Create Question serializer
    """

    class Meta:
        model = Question
        fields = ('question', 'type_question', 'score', 'lesson')
