# Generated by Django 4.1.3 on 2022-12-27 16:47

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
        ),
    ]