# Generated by Django 3.1.2 on 2020-11-17 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editari', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='isOnline',
            field=models.BooleanField(),
        ),
    ]