# Generated by Django 3.1 on 2020-08-07 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='questions',
            field=models.ManyToManyField(default=True, to='questions.Question'),
        ),
    ]