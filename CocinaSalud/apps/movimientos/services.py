from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import Http404
from apps.curso.models import CursoUsuario, LeccionUsuario, Leccion
from apps.usuario_custom.models import Usuario
from .models import Movimiento, MedioDePago

def create_movimiento(
        curso, usuario: Usuario, paypal_mdp: MedioDePago, codigo_operacion: str
    ) -> Movimiento:
    """
    Crea una nueva instancia de Movimiento, teniendo en cuenta si es un curso o el programa
    """
    if curso:
        return Movimiento.objects.create(
            usuario=usuario,
            curso=curso,
            medio_de_pago=paypal_mdp,
            importe=curso.precio,
            descripcion=f'Compra curso {curso.nombre} por parte de {usuario.get_username()} a través de {paypal_mdp.nombre}',
            condicion=Movimiento.ESTADO_INICIADA,
            codigo_operacion=codigo_operacion
        )
    return Movimiento.objects.create(
        usuario=usuario,
        medio_de_pago=paypal_mdp,
        importe=30,
        descripcion=f'Compra programa de nutrición por parte de {usuario.get_username()} a través de {paypal_mdp.nombre}',
        condicion=Movimiento.ESTADO_INICIADA,
        codigo_operacion=codigo_operacion
    )


def create_curso_lecciones_usuario(user, curso) -> None:
    usuario = Usuario.objects.get(user=user, state=True)
    CursoUsuario.objects.create(
        curso=curso,
        usuario=usuario,
    )
    lecciones = Leccion.objects.filter(
        state=True,
        seccion__curso=curso
    )

    for leccion in lecciones:
        LeccionUsuario.objects.create(
            leccion=leccion,
            usuario=usuario
        )


def finalizar_compra(user, movimiento) -> None:
    curso = movimiento.curso

    if curso:
        try:
            create_curso_lecciones_usuario(user, curso)
        except Usuario.DoesNotExist:
            raise Http404('Usuario no encontrado')

        # Modify number of students registered in the course
        curso.num_alumnos = F('num_alumnos') + 1
        curso.save()
    else:
        usuario = get_object_or_404(Usuario, user=user)
        usuario.compro_gestoria = True
        usuario.save()



    