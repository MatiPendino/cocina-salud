from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Salud, ItemSalud

class SaludIndex(ListView):
    template_name = 'blog/salud.html'
    model = Salud
    context_object_name = 'salud_posts'
    queryset = Salud.objects.filter(state=True)


def ver_salud(request, salud_slug):
    salud = Salud.objects.filter(slug=salud_slug).first()
    items_salud = ItemSalud.objects.filter(salud=salud).order_by('numero_item')

    if not salud:
        return redirect('salud')

    context = {
        'salud': salud,
        'items': items_salud,
    }

    return render(request, 'blog/salud_detalle.html', context)