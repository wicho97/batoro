# Generated by Django 4.2.5 on 2023-11-08 22:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_attachment_mime_type_attachment_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentary',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]