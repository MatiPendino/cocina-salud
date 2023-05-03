from django.db import models
from ckeditor.fields import RichTextField
from apps.base.models import BaseModel
from apps.usuario_custom.models import Usuario


class Curso(BaseModel):
    nombre = models.CharField('Nombre del curso', max_length=255) 
    imagen_curso = models.ImageField('Imagen del curso', null=True, blank=True, upload_to='curso')
    precio = models.DecimalField('Precio del curso', max_digits=10, decimal_places=2)
    publico_dirigido = RichTextField('Público dirigido', null=True, blank=True)
    aprender = RichTextField('Qué aprenderá', null=True, blank=True)
    descripcion_breve = models.CharField('Descripción breve', max_length=255)
    descripcion_extensa = RichTextField('Descripción extensa', null=True, blank=True)
    calificacion = models.DecimalField('Calificación del curso', max_digits=3, decimal_places=2, default=0)
    num_alumnos = models.PositiveIntegerField('Número de alumnos', default=0)
    profesor = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Profesor del curso')

    def __str__(self):
        return f'{self.nombre} ({self.calificacion}) - {self.profesor.get_username()}'

    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'


class Seccion(BaseModel):
    nombre = models.CharField('Nombre de sección', max_length=255)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name='Curso de la sección')
    orden = models.PositiveSmallIntegerField('Orden de la sección')

    def get_curso_nombre(self):
        return self.curso.nombre
    
    def __str__(self):
        return f'{self.nombre} - {self.curso.nombre}'
    
    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'


class Leccion(BaseModel):
    nombre = models.CharField('Nombre de lección', max_length=255)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, verbose_name='Sección de la lección')
    descripcion = RichTextField('Descripción de lección', null=True, blank=True)
    duracion = models.PositiveSmallIntegerField('Duración de lección', help_text='Duración de la lección (en minutos)', default=0)
    video = models.URLField('Video de la lección', help_text='Insertar la URL del video de la lección', null=True, blank=True)
    orden = models.PositiveSmallIntegerField('Orden de la lección')

    def get_seccion_nombre(self):
        return self.seccion.nombre
    
    def get_curso_nombre(self):
        return self.seccion.curso.nombre
    
    def __str__(self):
        return f'{self.get_curso_nombre()} - {self.nombre}'
    
    class Meta:
        verbose_name = 'Lección'
        verbose_name_plural = 'Lecciones'


class CursoUsuario(BaseModel):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.DecimalField('Calificación del usuario', max_digits=3, decimal_places=2, default=0)
    opinion = RichTextField('Opinión del curso', null=True, blank=True)

    def __str__(self):
        return f'{self.curso.nombre} - {self.usuario.get_username()}'
    
    class Meta:
        verbose_name = 'Curso Usuario'
        verbose_name_plural = 'Cursos Usuarios'


class LeccionUsuario(BaseModel):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    completada = models.BooleanField('Lección completada', default=False)

    def __str__(self):
        return f'{self.leccion.nombre} ({self.leccion.get_curso_nombre()}) - {self.usuario.get_username()}'
    
    class Meta:
        verbose_name = 'Lección Usuario'
        verbose_name_plural = 'Lecciones Usuarios'