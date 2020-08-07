# Djangorestframework
from rest_framework import viewsets

# Models and Serializers
from .models import Question
from .serializers import QuestionSerializer, CreateQuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    # Over write serializer class
    def get_serializer_class(self):
        if self.action == 'create':
            return CreateQuestionSerializer
        return QuestionSerializer
