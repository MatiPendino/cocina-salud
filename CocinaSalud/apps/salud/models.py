from django.db import models

from apps.base.models import BaseModel

class Salud(BaseModel):
    titulo = models.CharField(max_length=255, null=True)
    intro = models.TextField(blank=True, null=True)
    imagen_principal = models.ImageField(upload_to='salud/', blank=True, null=True)
    imagen_secundaria_1 = models.ImageField(upload_to='salud/', blank=True, null=True)
    imagen_secundaria_2 = models.ImageField(upload_to='salud/', blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
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
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.salud}: ítem {self.numero_item}'

    class Meta:
        verbose_name = 'Ítem Salud'
        verbose_name_plural = 'Ítems Salud'
