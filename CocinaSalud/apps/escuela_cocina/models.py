from django.db import models

class EscuelaCocina(models.Model):
    titulo = models.CharField(max_length=255)
    imagen = models.ImageField()
    resumen = models.TextField()

    class Meta:
        verbose_name_plural = "Artículos de Escuela de Cocina"
        verbose_name = "Artículo de Escuela de Cocina"
