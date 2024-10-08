from django.db import models

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    state = models.BooleanField('Estado', default=True)
    creation_date = models.DateField('Fecha creación', auto_now_add=True, auto_now=False, blank=True, null=True)
    updating_date = models.DateField('Fecha actualización', auto_now_add=False, auto_now=True, blank=True, null=True)
    deleting_date = models.DateField('Fecha eliminación', auto_now_add=False, auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True