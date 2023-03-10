# Generated by Django 4.1.3 on 2023-02-15 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EscuelaCocina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('imagen', models.ImageField(upload_to='')),
                ('resumen', models.TextField()),
            ],
            options={
                'verbose_name': 'Artículo de Escuela de Cocina',
                'verbose_name_plural': 'Artículos de Escuela de Cocina',
            },
        ),
    ]
