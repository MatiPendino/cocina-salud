from django.db import models
from ckeditor.fields import RichTextField
from apps.base.models import BaseModel
from apps.usuario_custom.models import Usuario
from .managers import LeccionManager, CursoUsuarioManager


class Curso(BaseModel):
    nombre = models.CharField('Nombre del curso', max_length=255) 
    imagen_curso = models.ImageField('Imagen del curso', null=True, blank=True, upload_to='curso')
    precio = models.DecimalField('Precio del curso', max_digits=10, decimal_places=2)
    slug = models.SlugField('Slug del curso', null=True, blank=True, unique=True, help_text='Debe ser escrito todo en minúsculas y sin espacios')
    publico_dirigido = RichTextField('Público dirigido', null=True, blank=True)
    aprender = RichTextField('Qué aprenderá', null=True, blank=True)
    descripcion_breve = models.CharField('Descripción breve', max_length=255)
    descripcion_extensa = RichTextField('Descripción extensa', null=True, blank=True)
    calificacion = models.DecimalField('Calificación del curso', max_digits=3, decimal_places=2, default=0)
    num_alumnos = models.PositiveIntegerField('Número de alumnos', default=0)
    num_calificaciones = models.PositiveIntegerField('Número de calificaciones', default=0)
    profesor = models.ForeignKey(Usuario, on_delete=models.SET_NULL, verbose_name='Profesor del curso', null=True)


    def get_cantidad_lecciones(self):
        lecciones_count = Leccion.objects.filter(seccion__curso__id=self.id).count()
        return lecciones_count
    
    def get_duracion_curso(self):
        # Obtenemos todas las lecciones del curso actual, y su duración en horas
        lecciones = Leccion.objects.filter(seccion__curso__id=self.id).values_list('duracion', flat=True)
        duracion_horas = sum(lecciones) / 60
        # Separamos en parte decimal y entera
        decimal_part = duracion_horas % 1
        integer_part = duracion_horas // 1
        # Según el valor de la parte decimal, redondeamos la duración total
        if decimal_part < 0.3:
            duracion = int(integer_part)
        elif 0.3 <= decimal_part < 0.7:
            duracion = integer_part + 0.5
        else:
            duracion = int(integer_part + 1)
        return duracion
    
    def get_secciones(self):
        return Seccion.objects.filter(curso__id=self.id, state=True)
    
    def get_porcentaje_completado_curso(self, user):
        lecciones_usuario = LeccionUsuario.objects.filter(usuario__user=user, leccion__seccion__curso=self, completada=True).count()
        return int(lecciones_usuario / self.get_cantidad_lecciones() * 100) if self.get_cantidad_lecciones() > 0 else 100
    
    def get_cantidad_cursos_usuarios(self):
        num_cursos_usuarios = CursoUsuario.objects.filter(curso=self).count()
        return num_cursos_usuarios
    
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
    
    def get_lecciones(self):
        return Leccion.objects.filter(seccion__id=self.id, state=True)
    
    def get_lecciones_usuario(self):
        return LeccionUsuario.objects.filter(leccion__seccion__id=self.id, state=True)
    
    def __str__(self):
        return f'{self.nombre} - {self.curso.nombre}'
    
    class Meta:
        verbose_name = 'Sección'
        verbose_name_plural = 'Secciones'


class Leccion(BaseModel):
    nombre = models.CharField('Nombre de lección', max_length=255)
    slug = models.SlugField('Slug de la lección', blank=True, null=True, unique=True, help_text='Debe ser escrito todo en minúsculas y sin espacios')
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, verbose_name='Sección de la lección')
    descripcion = RichTextField('Descripción de lección', null=True, blank=True)
    duracion = models.PositiveSmallIntegerField('Duración de lección', help_text='Duración de la lección (en minutos)', default=0)
    video_id = models.CharField('Video de la lección', help_text='Insertar el id del video de la lección', null=True, blank=True, max_length=20)
    orden = models.PositiveSmallIntegerField('Orden de la lección')

    objects = LeccionManager()

    def get_seccion_nombre(self):
        return self.seccion.nombre
    
    def get_curso_nombre(self):
        return self.seccion.curso.nombre
    
    def get_secciones_curso(self):
        curso = Curso.objects.filter(id=self.seccion.curso.id).first()
        return curso.get_secciones()
    
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

    objects = CursoUsuarioManager()

    def __str__(self):
        return f'{self.curso.nombre} - {self.usuario.get_username()}'
    
    class Meta:
        verbose_name = 'Curso Usuario'
        verbose_name_plural = 'Cursos Usuarios'


class LeccionUsuario(BaseModel):
    leccion = models.ForeignKey(Leccion, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    completada = models.BooleanField('Lección completada', default=False)
    ultima = models.BooleanField('Última lección vista por el usuario', default=False)

    def get_leccion_nombre(self):
        return self.leccion.nombre
    
    def complete_lesson(self):
        self.completada = True
        self.save()

    def __str__(self):
        return f'{self.leccion.nombre} ({self.leccion.get_curso_nombre()}) - {self.usuario.get_username()}'
    
    class Meta:
        verbose_name = 'Lección Usuario'
        verbose_name_plural = 'Lecciones Usuarios'