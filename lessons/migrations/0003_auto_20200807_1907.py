# Generated by Django 3.1 on 2020-08-07 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
        ('lessons', '0002_auto_20200807_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='questions',
            field=models.ManyToManyField(default=False, to='questions.Question'),
        ),
    ]
