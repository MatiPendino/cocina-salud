from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from .models import Movimiento
from apps.usuario_custom.models import Usuario
from .utils import get_movimiento_condicion, create_curso_lecciones_usuario, send_compra_via_email


def mis_movimientos(request):
    usuario = get_object_or_404(Usuario, user=request.user)
    movimientos = Movimiento.objects.filter(
        usuario=usuario
    )

    return render(request, 'mis_movimientos.html', {'movimientos': movimientos})


def compra_finalizada(request, course_slug, codigo_operacion):
    movimiento = get_object_or_404(Movimiento, codigo_operacion=codigo_operacion)

    context = {
        'movimiento': movimiento,
        'course_slug': course_slug
    }
    return render(request, 'compra_finalizada.html', context)


def compra_no_finalizada(request, course_slug, codigo_operacion):
    return render(request, 'compra_no_finalizada.html')


@never_cache
@csrf_exempt
def ipn(request, codigo_operacion):
    movimiento = get_object_or_404(Movimiento, codigo_operacion=codigo_operacion)

    movimiento.condicion = get_movimiento_condicion(request, movimiento)
    movimiento.save()

    if movimiento.condicion == Movimiento.ESTADO_FINALIZADA:
        try:
            send_compra_via_email(movimiento.usuario.user.email, movimiento.curso)
        except:
            print("Mail server not implemented yet")

        if movimiento.curso:
            create_curso_lecciones_usuario(request.user, movimiento.curso)

            # Modify number of students registered in the course
            movimiento.curso.num_alumnos +=1
            movimiento.curso.save()
        else:
            usuario = get_object_or_404(Usuario, user=request.user)
            usuario.compro_gestoria = True
            usuario.save()


        if movimiento.curso:
            return redirect(
                'compra_finalizada', 
                course_slug=movimiento.curso.slug, 
                codigo_operacion=codigo_operacion
            )
        return redirect(
            'compra_finalizada', 
            course_slug='programa', 
            codigo_operacion=codigo_operacion
        )
    else:
        return redirect(
            'compra_no_finalizada',
            course_slug=movimiento.curso.slug,
            codigo_operacion=codigo_operacion
        )


