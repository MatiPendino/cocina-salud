# Generated by Django 4.1.3 on 2023-09-23 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0006_leccion_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='num_calificaciones',
            field=models.PositiveIntegerField(default=0, verbose_name='Número de calificaciones'),
        ),
    ]
