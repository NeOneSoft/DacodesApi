# Django
from django.contrib import admin

# Models
from .models import Lesson


@admin.register(Lesson)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lesson', 'target_score')
