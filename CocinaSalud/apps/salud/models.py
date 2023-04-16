from django.db import models
from ckeditor.fields import RichTextField
from apps.base.models import BaseModel

class Salud(BaseModel):
    image_upload = 'salud/'

    titulo = models.CharField(max_length=255, null=True)
    intro = RichTextField(blank=True, null=True)
    imagen_principal = models.ImageField(upload_to=image_upload, blank=True, null=True)
    imagen_miniatura = models.ImageField(upload_to=image_upload, blank=True, null=True)
    imagen_secundaria_1 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    imagen_secundaria_2 = models.ImageField(upload_to=image_upload, blank=True, null=True)
    conclusion = RichTextField(blank=True, null=True)
    resumen = RichTextField(blank=True, null=True)
    youtube_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'Salud sobre {self.titulo}'
    
    class Meta:
        verbose_name_plural = 'Artículos de Salud'
        verbose_name = 'Artículo de Salud'


class ItemSalud(BaseModel):
    titulo = models.CharField(max_length=255)
    numero_item = models.PositiveSmallIntegerField()
    salud = models.ForeignKey(Salud, on_delete=models.CASCADE)
    descripcion = RichTextField()

    def __str__(self):
        return f'{self.salud}: ítem {self.numero_item}'

    class Meta:
        verbose_name = 'Ítem Salud'
        verbose_name_plural = 'Ítems Salud'
