# Django
from django.test import TestCase

# Model Course test
from .models import Lesson


class CourseModelTest(TestCase):

    def create_lesson(self, lesson="Lesson_test", target_score=90):
        return Lesson.objects.create(lesson=lesson, target_score=target_score)

    def test_lesson_creation(self):
        lesson = self.create_lesson()
        self.assertTrue(isinstance(lesson, Lesson))
        self.assertEqual(lesson.__str__(), lesson.lesson)