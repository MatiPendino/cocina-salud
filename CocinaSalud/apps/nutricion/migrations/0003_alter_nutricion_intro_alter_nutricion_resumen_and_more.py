# Generated by Django 4.1.3 on 2023-04-16 14:19

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutricion', '0002_nutricion_creation_date_nutricion_deleting_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutricion',
            name='intro',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='resumen',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='texto_cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nutricion',
            name='texto_explicativo',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]