from django.shortcuts import render
from django.views.generic import ListView

from .models import Nutricion

class NutricionIndex(ListView):
    template_name = 'nutricion.html'
    model = Nutricion
    context_object_name = 'nutricion_posts'
    queryset = Nutricion.objects.all()


def ver_nutricion(request, nutricion_id):
    nutricion = Nutricion.objects.filter(id=nutricion_id).first()

    context = {
        'nutricion': nutricion,
    }

    return render(request, 'nutricion_detalle.html', context)