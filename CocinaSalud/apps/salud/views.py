from django.shortcuts import render
from django.views.generic import ListView

from .models import Salud, ItemSalud

class SaludIndex(ListView):
    template_name = 'salud.html'
    model = Salud
    context_object_name = 'salud_posts'
    queryset = Salud.objects.all()


def ver_salud(request, salud_id):
    salud = Salud.objects.filter(id=salud_id).first()
    items_salud = ItemSalud.objects.filter(salud__id=salud_id).order_by('numero_item')

    context = {
        'salud': salud,
        'items': items_salud,
    }

    return render(request, 'salud_detalle.html', context)