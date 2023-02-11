from django.db import models

class Receta(models.Model):
    titulo = models.CharField(max_length=255)
    imagen_principal = models.ImageField()
    resumen = models.TextField(blank=True)
    ingredientes = models.TextField(blank=True)
    instrucciones = models.TextField(blank=True)
    composicion_nutricional = models.TextField(blank=True)
    duracion = models.IntegerField(blank=True)
    imagen_secundaria_1 = models.ImageField(blank=True)
    imagen_secundaria_2 = models.ImageField(blank=True)
    imagen_secundaria_3 = models.ImageField(blank=True)
    youtube_link = models.URLField(blank=True)

    def __str__(self):
        return f"Receta de {self.titulo}"
