from django.db import models

from apps.base.models import BaseModel

class Nutricion(BaseModel):
    titulo = models.CharField(max_length=255, null=True)
    imagen_principal = models.ImageField(upload_to='nutricion/', blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    texto_cuerpo = models.TextField(blank=True, null=True)
    imagen_secundaria_1 = models.ImageField(upload_to='nutricion/', blank=True, null=True)
    imagen_secundaria_2 = models.ImageField(upload_to='nutricion/', blank=True, null=True)
    texto_explicativo = models.TextField(blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    youtube_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Nutrición sobre {self.titulo}'
    
    class Meta:
        verbose_name_plural = 'Artículos de Nutrición'
        verbose_name = 'Artículo de Nutrición'
