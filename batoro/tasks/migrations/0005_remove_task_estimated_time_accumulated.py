# Generated by Django 4.2.5 on 2023-11-06 17:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_task_estimated_time_accumulated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='estimated_time_accumulated',
        ),
    ]