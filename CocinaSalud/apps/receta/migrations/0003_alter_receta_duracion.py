# Generated by Django 4.1.3 on 2023-09-17 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0002_receta_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receta',
            name='duracion',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
