# Generated by Django 4.1.3 on 2023-05-10 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario_custom', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='profesion',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Profesión del usuario'),
        ),
    ]