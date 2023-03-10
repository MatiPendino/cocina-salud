# Generated by Django 4.1.3 on 2023-02-25 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('receta', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='receta',
            options={'verbose_name': 'Receta', 'verbose_name_plural': 'Recetas'},
        ),
        migrations.RemoveField(
            model_name='receta',
            name='instrucciones',
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen_principal',
            field=models.ImageField(upload_to='recetas/'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen_secundaria_1',
            field=models.ImageField(blank=True, upload_to='recetas/'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen_secundaria_2',
            field=models.ImageField(blank=True, upload_to='recetas/'),
        ),
        migrations.AlterField(
            model_name='receta',
            name='imagen_secundaria_3',
            field=models.ImageField(blank=True, upload_to='recetas/'),
        ),
        migrations.CreateModel(
            name='PasoReceta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, verbose_name='Fecha eliminación')),
                ('titulo', models.CharField(max_length=255)),
                ('numero_paso', models.PositiveSmallIntegerField()),
                ('descripcion', models.TextField()),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='receta.receta')),
            ],
            options={
                'verbose_name': 'Paso receta',
                'verbose_name_plural': 'Pasos receta',
            },
        ),
    ]
