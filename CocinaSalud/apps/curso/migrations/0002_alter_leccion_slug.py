# Generated by Django 4.1.3 on 2023-06-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leccion',
            name='slug',
            field=models.SlugField(help_text='Debe ser escrito todo en minúsculas y sin espacios', verbose_name='Slug de la lección'),
        ),
    ]
