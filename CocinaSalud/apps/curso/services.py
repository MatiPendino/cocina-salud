

from apps.curso.selectors import get_lecciones_usuario
from apps.curso.utils import get_lessons_for_section, get_percentage_rating


def get_estrellas(cursos_usuarios):
    calificaciones = list(cursos_usuarios.values_list('calificacion', flat=True))
    # Obtenemos la cantidad de usuarios que puntuaron cada estrella
    una_estrella, dos_estrellas, tres_estrellas, cuatro_estrellas, cinco_estrellas = [
        calificaciones.count(calificacion) for calificacion in range(1, 6)
    ]

    num_total_estrellas = sum([
        una_estrella, dos_estrellas, tres_estrellas, cuatro_estrellas, cinco_estrellas
    ])

    una_estrella_p, dos_estrellas_p, tres_estrellas_p, cuatro_estrellas_p, cinco_estrellas_p = [
        get_percentage_rating(num_estrella, num_total_estrellas) for num_estrella in range(1, 6)
    ]

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

def get_secciones_lecciones_usuario(lesson, user, curso):
    # Obtain all the course sections and the user lessons
    secciones = list(lesson.get_secciones_curso())
    lecciones_usuario = get_lecciones_usuario(user=user, curso=curso).order_by('leccion__orden')

    # Creation of a dictionary where the keys are the section names, and values
    # their corresponding list of user lessons
    secciones_lecciones_usuario = {
        seccion.nombre: get_lessons_for_section(lecciones_usuario, seccion)
        for seccion in secciones
    }

    return secciones_lecciones_usuario