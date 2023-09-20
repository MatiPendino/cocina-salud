from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Nutricion

class NutricionIndex(ListView):
    template_name = 'blog/nutricion.html'
    model = Nutricion
    context_object_name = 'nutricion_posts'
    queryset = Nutricion.objects.filter(state=True)


def ver_nutricion(request, nutricion_slug):
    nutricion = Nutricion.objects.filter(slug=nutricion_slug).first()

    if not nutricion:
        return redirect('nutricion')

    context = {
        'nutricion': nutricion,
    }

    return render(request, 'blog/nutricion_detalle.html', context)