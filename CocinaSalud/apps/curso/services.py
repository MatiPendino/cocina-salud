from apps.curso.selectors import get_lecciones_usuario
from apps.curso.utils import get_leccion_usuario_por_seccion, get_porcentaje_estrella
from apps.curso.models import LeccionUsuario, CursoUsuario

def get_estrellas(cursos_usuarios):
    estrellas_range = range(1, 6)
    calificaciones = list(cursos_usuarios.values_list('calificacion', flat=True))
    # Obtenemos la cantidad de usuarios que puntuaron cada estrella
    una_estrella, dos_estrellas, tres_estrellas, cuatro_estrellas, cinco_estrellas = [
        calificaciones.count(calificacion) for calificacion in estrellas_range
    ]

    num_total_estrellas = sum([
        una_estrella, dos_estrellas, tres_estrellas, cuatro_estrellas, cinco_estrellas
    ])

    una_estrella_p = get_porcentaje_estrella(una_estrella, num_total_estrellas)
    dos_estrellas_p = get_porcentaje_estrella(dos_estrellas, num_total_estrellas)
    tres_estrellas_p = get_porcentaje_estrella(tres_estrellas, num_total_estrellas)
    cuatro_estrellas_p = get_porcentaje_estrella(cuatro_estrellas, num_total_estrellas)
    cinco_estrellas_p = get_porcentaje_estrella(cinco_estrellas, num_total_estrellas)

    return {
        'una_estrella': una_estrella,
        'dos_estrellas': dos_estrellas,
        'tres_estrellas': tres_estrellas,
        'cuatro_estrellas': cuatro_estrellas,
        'cinco_estrellas': cinco_estrellas,
        'una_estrella_p': una_estrella_p,
        'dos_estrellas_p': dos_estrellas_p,
        'tres_estrellas_p': tres_estrellas_p,
        'cuatro_estrellas_p': cuatro_estrellas_p,
        'cinco_estrellas_p': cinco_estrellas_p,
        'num_total_estrellas': num_total_estrellas
    }


def get_secciones_lecciones_usuario(user, curso):
    """
    Retorna un diccionario que contiene el nombre de las secciones como clave,
    y las lecciones de la seccion como valor
    """
    # Obtain all the course sections and the user lessons
    secciones = list(curso.get_secciones())
    lecciones_usuario = get_lecciones_usuario(user=user, curso=curso).order_by('leccion__orden')

    secciones_lecciones_usuario = {
        seccion.nombre: get_leccion_usuario_por_seccion(lecciones_usuario, seccion)
        for seccion in secciones
    }
    return secciones_lecciones_usuario


def update_last_seen_leccion_usuario(user, leccion):
    """
    Actualiza el valor de la última lección vista por el usuario

    Cambia el valor de la anterior instancia de LeccionUsuario a False, y
    el de la nueva instancia a True
    """
    curso = leccion.seccion.curso

    # Remove the "last" check in the previous seen user lesson
    last_seen_user_lesson = LeccionUsuario.objects.filter(
        usuario__user=user,
        leccion__seccion__curso=curso,
        ultima=True
    ).first()
    if last_seen_user_lesson:
        last_seen_user_lesson.ultima = False
        last_seen_user_lesson.save()

    # Add the "last" check in the current user lesson
    current_user_lesson = LeccionUsuario.objects.filter(
        usuario__user=user,
        leccion=leccion,
        state=True
    ).first()
    current_user_lesson.ultima = True
    current_user_lesson.save()


def dejar_resenia(curso_usuario_id, rating, comment):
    """
    Si el usuario deja una resenia, se actualiza la instancia de CursoUsuario y
    la calificación promedio del curso
    """
    curso_usuario = CursoUsuario.objects.filter(id=curso_usuario_id).first()
    curso = curso_usuario.curso
    rating = rating
    opinion = comment
    if curso_usuario:
        curso_usuario.calificacion = rating
        curso_usuario.opinion = opinion
        curso_usuario.save()

    cursos_usuarios = CursoUsuario.objects.filter(state=True, curso=curso, calificacion__gte=1)
    sum_stars = sum([curso_usuario.calificacion for curso_usuario in cursos_usuarios])
    average_calification = round(sum_stars/len(cursos_usuarios), 2)
    curso.calificacion = average_calification
    curso.save()