# Generated by Django 3.1.2 on 2020-12-08 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editari', '0002_teacher_is_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='is_teacher',
        ),
    ]