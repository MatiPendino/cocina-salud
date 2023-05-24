from django.shortcuts import redirect, render
from django.views.generic import ListView

from apps.escuela_cocina.models import EscuelaCocina, PasoTecnica


class EscuelaCocinaIndex(ListView):
    template_name = 'blog/escuela_cocina.html'
    model = EscuelaCocina
    context_object_name = 'escuelas_cocina'
    queryset = EscuelaCocina.objects.filter(state=True)


def ver_escuela_cocina(request, escuela_id):
    escuela_cocina = EscuelaCocina.objects.filter(id=escuela_id).first()
    pasos_escuela = PasoTecnica.objects.filter(escuela_cocina=escuela_cocina).order_by('numero_paso')

    if not escuela_cocina:
        return redirect('escuela_cocina')

    context = {
        'escuela_cocina': escuela_cocina,
        'pasos_escuela': pasos_escuela
    }

    return render(request, 'blog/escuela_cocina_detalle.html', context)