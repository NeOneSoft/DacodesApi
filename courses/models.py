# Django
from django.db import models
from django.contrib.auth.models import User


class Course(models.Model):
    course = models.CharField(max_length=200)
    students = models.ManyToManyField(User)

    def __str__(self):
        return self.course
