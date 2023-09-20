from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *


class RecetasIndex(ListView):
    template_name = 'blog/recetas.html'
    model = Receta
    context_object_name = 'recetas'
    queryset = Receta.objects.filter(state=True)


def ver_receta(request, receta_slug):
    receta = Receta.objects.filter(slug=receta_slug).first()
    pasos_receta = PasoReceta.objects.filter(receta__slug=receta_slug).order_by('numero_paso')

    if not receta:
        return redirect('recetas')

    # La imagen secundaria horizontal aparecerá entre medio de las instrucciones
    if pasos_receta.count() % 2 == 0:
        posicion_imagen = pasos_receta.count() / 2
    else:
        posicion_imagen = (pasos_receta.count() + 1) / 2

    context = {
        'receta': receta,
        'pasos': pasos_receta,
        'posicion_imagen': posicion_imagen
    }

    return render(request, 'blog/receta_detalle.html', context)