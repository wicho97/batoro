# Generated by Django 4.2.5 on 2023-11-06 22:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tasks", "0005_remove_task_estimated_time_accumulated"),
    ]

    operations = [
        migrations.AddField(
            model_name="attachment",
            name="mime_type",
            field=models.CharField(default="image/jpeg", max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="attachment",
            name="size",
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
