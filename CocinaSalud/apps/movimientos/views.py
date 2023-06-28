from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from apps.curso.models import CursoUsuario, LeccionUsuario, Leccion
from apps.usuario_custom.models import Usuario
from .models import Movimiento, MedioDePago
from .implementations import impl_paypal
from .utils import get_movimiento_condicion, create_curso_lecciones_usuario


def compra_finalizada(request, course_slug, codigo_operacion):
    return render(request, 'compra_finalizada.html')


def compra_no_finalizada(request, course_slug, codigo_operacion):
    return render(request, 'compra_no_finalizada.html')


@never_cache
@csrf_exempt
def ipn(request, codigo_operacion):
    movimiento = Movimiento.objects.get(codigo_operacion=codigo_operacion)

    movimiento.condicion = get_movimiento_condicion(request, movimiento)
    movimiento.save()

    if movimiento.condicion == Movimiento.ESTADO_FINALIZADA:
        try:
            # send_compra_via_email()
            pass
        except:
            pass

        create_curso_lecciones_usuario(request.user, movimiento.curso)

        return redirect(
            'compra_finalizada', 
            course_slug=movimiento.curso.slug, 
            codigo_operacion=codigo_operacion
        )
    else:
        return redirect(
            'compra_no_finalizada',
            course_slug=movimiento.curso.slug,
            codigo_operacion=codigo_operacion
        )


