from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class RecetasIndex(ListView):
    template_name = 'recetas.html'
    model = Receta
    context_object_name = 'recetas'
    queryset = Receta.objects.all()


def ver_receta(request, receta_id):
    receta = Receta.objects.filter(id=receta_id).first()