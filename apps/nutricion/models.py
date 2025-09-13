from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from ckeditor.fields import RichTextField
from apps.base.models import BaseModel

class Nutricion(BaseModel):
    image_upload = 'nutricion/'

    titulo = models.CharField(max_length=255, null=True)
    slug = models.SlugField('Slug del artículo', null=True, blank=True, unique=True, help_text='Debe ser escrito todo en minúsculas y sin espacios')
    imagen_principal = models.ImageField(upload_to=image_upload, blank=True, null=True)
    imagen_miniatura = models.ImageField(upload_to=image_upload, blank=True, null=True)
    intro = RichTextField(blank=True, null=True)
    texto_cuerpo = RichTextField(blank=True, null=True)
    imagen_secundaria_1 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    imagen_secundaria_2 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    imagen_secundaria_3 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    texto_explicativo = RichTextField(blank=True, null=True)
    resumen = RichTextField(blank=True, null=True)
    youtube_id = models.CharField(
        blank=True, 
        null=True, 
        max_length=11, 
        validators=[MinLengthValidator(limit_value=11), MaxLengthValidator(limit_value=11)]
    )

    def __str__(self):
        return f'Nutrición sobre {self.titulo}'
    
    class Meta:
        verbose_name_plural = 'Artículos de Nutrición'
        verbose_name = 'Artículo de Nutrición'
