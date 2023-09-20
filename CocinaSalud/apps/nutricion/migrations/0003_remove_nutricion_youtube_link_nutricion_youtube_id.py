# Generated by Django 4.1.3 on 2023-09-17 09:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutricion', '0002_nutricion_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nutricion',
            name='youtube_link',
        ),
        migrations.AddField(
            model_name='nutricion',
            name='youtube_id',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.MinLengthValidator(limit_value=11), django.core.validators.MaxLengthValidator(limit_value=11)]),
        ),
    ]