# Generated by Django 3.1 on 2020-08-07 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0004_auto_20200807_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lesson',
            name='questions',
        ),
    ]