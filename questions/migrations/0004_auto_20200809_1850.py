# Generated by Django 3.1 on 2020-08-09 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='answer',
        ),
        migrations.AddField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(default='correct answer', max_length=200),
        ),
        migrations.AddField(
            model_name='question',
            name='user_answer',
            field=models.CharField(default='None', max_length=200),
        ),
    ]
