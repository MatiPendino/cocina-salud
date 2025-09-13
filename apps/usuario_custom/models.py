from django.db import models
from django.contrib.auth.models import User
from apps.base.models import BaseModel


class Usuario(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    imagen_perfil = models.ImageField('Foto de perfil', upload_to='usuario', null=True, blank=True)
    fecha_nacimiento = models.DateField('Fecha de nacimiento', null=True, blank=True)
    profesion = models.CharField('Profesión del usuario', max_length=255, blank=True, null=True)
    compro_gestoria = models.BooleanField('Compró gestoría', default=False)

    def get_username(self):
        return self.user.username

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfiles'