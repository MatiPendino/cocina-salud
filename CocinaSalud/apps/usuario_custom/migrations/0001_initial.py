# Generated by Django 4.1.3 on 2023-06-28 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha eliminación')),
                ('imagen_perfil', models.ImageField(blank=True, null=True, upload_to='usuario', verbose_name='Foto de perfil')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('profesion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Profesión del usuario')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Usuario Custom',
                'verbose_name_plural': 'Usuarios Custom',
            },
        ),
    ]
