from django.db import models

from apps.base.models import BaseModel

class Receta(BaseModel):
    titulo = models.CharField(max_length=255)
    imagen_principal = models.ImageField(upload_to='recetas/')
    resumen = models.TextField(blank=True)
    ingredientes = models.TextField(blank=True)
    composicion_nutricional = models.TextField(blank=True)
    duracion = models.IntegerField(blank=True)
    imagen_secundaria_1 = models.ImageField(blank=True, upload_to='recetas/')
    imagen_secundaria_2 = models.ImageField(blank=True, upload_to='recetas/')
    imagen_secundaria_3 = models.ImageField(blank=True, upload_to='recetas/')
    youtube_link = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Receta'
        verbose_name_plural = 'Recetas'

    def __str__(self):
        return f"Receta de {self.titulo}"
    

class PasoReceta(BaseModel):
    titulo = models.CharField(max_length=255)
    numero_paso = models.PositiveSmallIntegerField()
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.receta}: Paso {self.numero_paso}'

    class Meta:
        verbose_name = 'Paso receta'
        verbose_name_plural = 'Pasos receta'
