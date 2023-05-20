from django.db import models
from django.contrib.auth.models import User
from apps.base.models import BaseModel


class Usuario(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    imagen_perfil = models.ImageField('Foto de perfil', upload_to='usuario', null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')
    profesion = models.CharField('Profesión del usuario', max_length=255, blank=True, null=True)

    def get_username(self):
        return self.user.username

    def __str__(self):
        return f'{self.user.username}'
    
    class Meta:
        verbose_name = 'Usuario Custom'
        verbose_name_plural = 'Usuarios Custom'