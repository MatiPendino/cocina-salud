# Generated by Django 4.1.3 on 2023-06-13 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0003_alter_leccion_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leccion',
            name='slug',
        ),
    ]
