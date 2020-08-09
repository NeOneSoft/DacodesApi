# Django
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError

# Models
from lessons.models import Lesson

# Type question options
TYPE = [
    ('BOOLEAN', 'BOOLEAN'),
    ('MULTIPLE CHOICE, ONE ANSWER', 'MULTIPLE CHOICE, ONE ANSWER'),
    ('MULTIPLE CHOICE, MORE THAN ONE ANSWER', 'MULTIPLE CHOICE, MORE THAN ONE ANSWER'),
    ('MULTIPLE CHOICE, MORE THAN ONE ANSWER, ALL HAS TO BE CORRECT',
     'MULTIPLE CHOICE, MORE THAN ONE ANSWER, ALL HAS TO BE CORRECT')
]


class Question(models.Model):
    question = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200, default='correct answer')
    user_answer = models.CharField(max_length=200, default='correct answer')
    type_question = models.CharField(max_length=200, choices=TYPE)
    score = models.IntegerField(validators=[MaxValueValidator(10), MinValueValidator(1)])
    lesson = models.ManyToManyField(Lesson)

    # Validating the right user answer
    # Overwriting save() method
    def save(self, *args, **kwargs):
        self.full_clean()
        return super(Question, self).save(*args, **kwargs)

    # Define clean() method to validate value and discount fields
    def clean(self):
        super(Question, self).clean()
        if self.correct_answer != self.user_answer:
            raise ValidationError({'Incorrect answer': 'The answer is not correct'})

    def __str__(self):
        return self.question
