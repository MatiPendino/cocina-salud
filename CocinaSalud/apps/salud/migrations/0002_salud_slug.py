# Generated by Django 4.1.3 on 2023-09-17 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salud',
            name='slug',
            field=models.SlugField(blank=True, help_text='Debe ser escrito todo en minúsculas y sin espacios', null=True, verbose_name='Slug del artículo'),
        ),
    ]