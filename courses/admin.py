# Django
from django.contrib import admin

# Models
from .models import Course


@admin.register(Course)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['course']
