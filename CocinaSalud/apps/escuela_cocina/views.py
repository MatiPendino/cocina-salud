from django.shortcuts import render
from django.views.generic import ListView

from apps.escuela_cocina.models import EscuelaCocina, PasoTecnica


class EscuelaCocinaIndex(ListView):
    template_name = 'escuela_cocina.html'
    model = EscuelaCocina
    context_object_name = 'escuelas_cocina'
    queryset = EscuelaCocina.objects.all()


def ver_escuela_cocina(request, escuela_id):
    escuela_cocina = EscuelaCocina.objects.filter(id=escuela_id).first()
    pasos_escuela = PasoTecnica.objects.filter(escuela_cocina=escuela_cocina).order_by('numero_paso')

    context = {
        'escuela_cocina': escuela_cocina,
        'pasos_escuela': pasos_escuela
    }

    return render(request, 'escuela_cocina_detalle.html', context)