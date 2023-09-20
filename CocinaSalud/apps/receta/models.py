from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from ckeditor.fields import RichTextField
from apps.base.models import BaseModel

class Receta(BaseModel):
    image_upload = 'recetas/'

    titulo = models.CharField(max_length=255)
    slug = models.SlugField('Slug del artículo', null=True, blank=True, help_text='Debe ser escrito todo en minúsculas y sin espacios')
    imagen_principal = models.ImageField(upload_to=image_upload)
    imagen_miniatura = models.ImageField(upload_to=image_upload, blank=True, null=True)
    resumen = RichTextField(blank=True, null=True)
    ingredientes = RichTextField(blank=True, null=True)
    composicion_nutricional = RichTextField(blank=True, null=True)
    duracion = models.IntegerField(blank=True, null=True)
    imagen_secundaria_1 = models.ImageField(blank=True, upload_to=image_upload)
    imagen_secundaria_2 = models.ImageField(blank=True, upload_to=image_upload)
    imagen_secundaria_3 = models.ImageField(blank=True, upload_to=image_upload)
    imagen_secundaria_4 = models.ImageField(blank=True, upload_to=image_upload)
    youtube_id = models.CharField(
        blank=True, 
        null=True, 
        max_length=11, 
        validators=[MinLengthValidator(limit_value=11), MaxLengthValidator(limit_value=11)]
    )

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return f"Receta de {self.titulo}"
    

class PasoReceta(BaseModel):
    titulo = models.CharField(max_length=255)
    numero_paso = models.PositiveSmallIntegerField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    descripcion = RichTextField()

    def __str__(self):
        return f'{self.receta}: Paso {self.numero_paso}'

    class Meta:
        verbose_name = 'Paso receta'
        verbose_name_plural = 'Pasos receta'
