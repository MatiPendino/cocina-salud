from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import *


class RecetasIndex(ListView):
    template_name = 'recetas.html'
    model = Receta
    context_object_name = 'recetas'
    queryset = Receta.objects.all()


def ver_receta(request, receta_id):
    receta = Receta.objects.filter(id=receta_id).first()
    pasos_receta = PasoReceta.objects.filter(receta__id=receta_id).order_by('numero_paso')

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

    return render(request, 'receta_detalle.html', context)