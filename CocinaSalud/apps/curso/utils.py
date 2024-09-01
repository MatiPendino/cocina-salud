from decimal import Decimal
from django.shortcuts import get_object_or_404
from apps.curso.models import Curso

def get_porcentaje_estrella(num_veces_estrella: int, total_estrellas: int) -> Decimal:
    """Obtiene el porcentaje de elección de una estrella"""
    if total_estrellas > 0:
        perc_ratings = num_veces_estrella/total_estrellas*100
    else:
        perc_ratings = 0

    return round(perc_ratings, 2)


def get_leccion_usuario_por_seccion(lecciones_usuario, seccion) -> list:
    return [
        leccion_usuario for leccion_usuario in lecciones_usuario
        if leccion_usuario.leccion.seccion == seccion
    ]
            

def get_curso(curso_slug: str):
    """Obtiene el curso a partir del curso_slug. Si es el programa, retorna None"""
    if curso_slug == 'programa':
        return None
    return get_object_or_404(Curso, slug=curso_slug, state=True)


def get_precio_str(curso) -> str:
    if curso:
        return str(curso.precio).replace(',', '.')
    return '30.00'