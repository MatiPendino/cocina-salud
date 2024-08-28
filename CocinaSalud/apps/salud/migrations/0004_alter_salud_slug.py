# Generated by Django 4.1.3 on 2023-10-15 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salud', '0003_remove_salud_youtube_link_salud_youtube_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salud',
            name='slug',
            field=models.SlugField(blank=True, help_text='Debe ser escrito todo en minúsculas y sin espacios', null=True, unique=True, verbose_name='Slug del artículo'),
        ),
    ]