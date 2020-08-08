# Django
from django.contrib import admin

# Models
from .models import Question


@admin.register(Question)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('question', 'type_question', 'score')
