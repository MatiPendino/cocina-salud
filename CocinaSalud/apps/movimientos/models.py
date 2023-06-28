from django.db import models
from apps.usuario_custom.models import Usuario
from apps.base.models import BaseModel
from apps.curso.models import Curso


class MedioDePago(BaseModel):
    TIPO_NINGUNO = 0
    TIPO_PAYPAL = 1
    CODIGOS_TIPO = (
        (TIPO_NINGUNO, 'NINGUNO'),
        (TIPO_PAYPAL, 'PAYPAL')
    )
    
    nombre = models.CharField('Nombre del mdp', max_length=75)
    tipo = models.IntegerField('Tipo del mdp', default=0, choices=CODIGOS_TIPO)
    client_id = models.CharField(max_length=150)
    secret_key = models.CharField(max_length=300)
    moneda_codigo = models.CharField('Código de la moneda', max_length=5)
    test = models.BooleanField('Medio de prueba', default=True)

    def __str__(self):
        return f'{self.nombre} - {self.tipo} ({self.moneda_codigo})'
    
    class Meta:
        verbose_name = 'Medio de Pago'
        verbose_name_plural = 'Medios de Pago'


class Movimiento(BaseModel):
    ESTADO_INICIADA = 0
    ESTADO_FINALIZADA = 1
    ESTADO_NO_FINALIZADA = 2
    CODIGOS_ESTADO = (
        (ESTADO_INICIADA, 'INICIADA'),
        (ESTADO_FINALIZADA, 'FINALIZADA'),
        (ESTADO_NO_FINALIZADA, 'NO FINALIZADA')
    )

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    medio_de_pago = models.ForeignKey(MedioDePago, on_delete=models.CASCADE, null=True)
    importe = models.DecimalField('Importe del movimiento', max_digits=10, decimal_places=2)
    descripcion = models.CharField('Descripción del movimiento', max_length=255)
    condicion = models.IntegerField('Estado del movimiento', default=0, choices=CODIGOS_ESTADO)
    codigo_operacion = models.CharField('Código operación', max_length=20, null=True)
    
    def __str__(self):
        return f'{self.usuario.get_username()} - {self.curso.nombre}: {self.condicion}'
    
    class Meta:
        verbose_name = 'Movimiento'
        verbose_name_plural = 'Movimientos'