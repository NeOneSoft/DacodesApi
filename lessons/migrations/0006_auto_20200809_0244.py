# Generated by Django 3.1 on 2020-08-09 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0005_remove_lesson_questions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ['id']},
        ),
    ]