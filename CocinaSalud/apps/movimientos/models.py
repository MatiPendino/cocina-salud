from django.db import models
from apps.usuario_custom.models import Usuario
from apps.base.models import BaseModel


class Movimiento(BaseModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    importe = models.DecimalField('Importe del movimiento', max_digits=10, decimal_places=2)
    descripcion = models.CharField('Descripción del movimiento', max_length=255)
    
    def __str__(self):
        return f'{self.usuario.get_username()} (${self.importe}): {self.descripcion}'
    
    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'