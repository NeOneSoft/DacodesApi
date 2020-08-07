# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Models
from lessons.models import Lesson

#Type question options
TYPE = [
    ('BOOLEAN', 'BOOLEAN'),
    ('MULTIPLE CHOICE, ONE ANSWER', 'MULTIPLE CHOICE, ONE ANSWER'),
    ('MULTIPLE CHOICE, MORE THAN ONE ANSWER', 'MULTIPLE CHOICE, MORE THAN ONE ANSWER'),
    ('MULTIPLE CHOICE, MORE THAN ONE ANSWER, ALL HAS TO BE CORRECT',
     'MULTIPLE CHOICE, MORE THAN ONE ANSWER, ALL HAS TO BE CORRECT')
]


class Question(models.Model):
    question = models.CharField(max_length=200)
    lesson_question = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    type_question = models.CharField(max_length=200, choices=TYPE)
    score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return self.question
