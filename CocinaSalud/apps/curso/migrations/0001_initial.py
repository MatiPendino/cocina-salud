# Generated by Django 4.1.3 on 2023-06-08 15:52

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuario_custom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del curso')),
                ('imagen_curso', models.ImageField(blank=True, null=True, upload_to='curso', verbose_name='Imagen del curso')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del curso')),
                ('slug', models.SlugField(blank=True, help_text='Debe ser escrito todo en minúsculas y sin espacios', null=True, verbose_name='Slug del curso')),
                ('publico_dirigido', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Público dirigido')),
                ('aprender', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Qué aprenderá')),
                ('descripcion_breve', models.CharField(max_length=255, verbose_name='Descripción breve')),
                ('descripcion_extensa', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción extensa')),
                ('calificacion', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Calificación del curso')),
                ('num_alumnos', models.PositiveIntegerField(default=0, verbose_name='Número de alumnos')),
                ('profesor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_custom.usuario', verbose_name='Profesor del curso')),
            ],
            options={
                'verbose_name': 'Curso',
                'verbose_name_plural': 'Cursos',
            },
        ),
        migrations.CreateModel(
            name='Leccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de lección')),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción de lección')),
                ('duracion', models.PositiveSmallIntegerField(default=0, help_text='Duración de la lección (en minutos)', verbose_name='Duración de lección')),
                ('video', models.URLField(blank=True, help_text='Insertar la URL del video de la lección', null=True, verbose_name='Video de la lección')),
                ('orden', models.PositiveSmallIntegerField(verbose_name='Orden de la lección')),
                ('slug', models.SlugField(verbose_name='Slug de la lección')),
            ],
            options={
                'verbose_name': 'Lección',
                'verbose_name_plural': 'Lecciones',
            },
        ),
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha eliminación')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre de sección')),
                ('orden', models.PositiveSmallIntegerField(verbose_name='Orden de la sección')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso', verbose_name='Curso de la sección')),
            ],
            options={
                'verbose_name': 'Sección',
                'verbose_name_plural': 'Secciones',
            },
        ),
        migrations.CreateModel(
            name='LeccionUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha eliminación')),
                ('completada', models.BooleanField(default=False, verbose_name='Lección completada')),
                ('ultima', models.BooleanField(default=False, verbose_name='Última lección vista por el usuario')),
                ('leccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.leccion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_custom.usuario')),
            ],
            options={
                'verbose_name': 'Lección Usuario',
                'verbose_name_plural': 'Lecciones Usuarios',
            },
        ),
        migrations.AddField(
            model_name='leccion',
            name='seccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.seccion', verbose_name='Sección de la lección'),
        ),
        migrations.CreateModel(
            name='CursoUsuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('creation_date', models.DateField(auto_now_add=True, null=True, verbose_name='Fecha creación')),
                ('updating_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha actualización')),
                ('deleting_date', models.DateField(auto_now=True, null=True, verbose_name='Fecha eliminación')),
                ('calificacion', models.DecimalField(decimal_places=2, default=0, max_digits=3, verbose_name='Calificación del usuario')),
                ('opinion', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Opinión del curso')),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curso.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuario_custom.usuario')),
            ],
            options={
                'verbose_name': 'Curso Usuario',
                'verbose_name_plural': 'Cursos Usuarios',
            },
        ),
    ]
