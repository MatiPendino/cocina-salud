# Generated by Django 4.1.3 on 2023-04-16 14:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0003_alter_pasoreceta_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasoreceta',
            name='descripcion',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='receta',
            name='composicion_nutricional',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='ingredientes',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='receta',
            name='resumen',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
