# Generated by Django 4.2.5 on 2023-10-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_status_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='color',
            field=models.CharField(default='#000000', max_length=7),
        ),
    ]
