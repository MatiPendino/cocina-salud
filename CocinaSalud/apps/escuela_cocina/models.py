from django.db import models

from apps.base.models import BaseModel 

class EscuelaCocina(BaseModel):
    titulo = models.CharField(max_length=255)
    imagen_principal = models.ImageField(upload_to='escuela_cocina/', blank=True, null=True)
    resumen = models.TextField(blank=True, null=True)
    ingredientes = models.TextField(blank=True, null=True)
    imagen_secundaria_1 = models.ImageField(blank=True, upload_to='escuela_cocina/', null=True)
    imagen_secundaria_2 = models.ImageField(blank=True, upload_to='escuela_cocina/', null=True)
    imagen_secundaria_3 = models.ImageField(blank=True, upload_to='escuela_cocina/', null=True)
    youtube_link = models.URLField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'Truco de cocina: {self.titulo}'

    class Meta:
        verbose_name_plural = "Artículos de Escuela de Cocina"
        verbose_name = "Artículo de Escuela de Cocina"


class PasoTecnica(BaseModel):
    titulo = models.CharField(max_length=255)
    numero_paso = models.PositiveSmallIntegerField()
    escuela_cocina = models.ForeignKey(EscuelaCocina, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.escuela_cocina}: Paso {self.numero_paso}'
    
    class Meta:
        verbose_name = 'Paso técnica'
        verbose_name_plural = 'Pasos técnica'
