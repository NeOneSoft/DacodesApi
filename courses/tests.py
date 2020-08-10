# Django
from django.test import TestCase

# Model Course test
from .models import Course


class CourseModelTest(TestCase):

    def create_course(self, course="Course_test"):
        return Course.objects.create(course=course)

    def test_course_creation(self):
        course = self.create_course()
        self.assertTrue(isinstance(course, Course))
        self.assertEqual(course.__str__(), course.course)


