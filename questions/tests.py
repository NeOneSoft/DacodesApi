# Django
from django.test import TestCase

# Model Course test
from .models import Question


class QuestionModelTest(TestCase):

    def create_question(self, question="Question_test", type_question="BOOLEAN", score=8):
        return Question.objects.create(question=question, type_question=type_question, score=score)

    def test_question_creation(self):
        question = self.create_question()
        self.assertTrue(isinstance(question, Question))
        self.assertEqual(question.__str__(), question.question)
