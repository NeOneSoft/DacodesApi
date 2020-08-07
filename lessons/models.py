# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Models
from courses.models import Course


class Lesson(models.Model):
    lesson = models.CharField(max_length=200)
    course_lesson = models.ForeignKey(Course, on_delete=models.CASCADE)
    target_score = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])

    def __str__(self):
        return self.lesson
