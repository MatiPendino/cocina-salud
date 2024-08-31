from django.shortcuts import get_object_or_404
from apps.curso.models import Leccion, CursoUsuario, Curso

def get_percentage_rating(rating, num_ratings):
    if num_ratings > 0:
        perc_ratings = rating/num_ratings*100
    else:
        perc_ratings = 0

    return round(perc_ratings, 2)


def get_leccion_usuario_por_seccion(lecciones_usuario, seccion):
    return [
        leccion_usuario for leccion_usuario in lecciones_usuario
        if leccion_usuario.leccion.seccion == seccion
    ]


def has_user_course(user, course):
    if user.is_authenticated:
        user_course = CursoUsuario.objects.filter(
            usuario__user=user,
            curso=course
        )
        return user_course.exists()
    
    return False


def get_slug_lesson_to_pass(lesson, direction):
    if direction == 'next':
        # If there is a following lesson in the section, return its id. Otherwise,
        # pass to the next section.
        next_lesson = Leccion.objects.filter(
            seccion=lesson.seccion,
            orden=lesson.orden+1
        ).first()
        if next_lesson:
            return next_lesson.slug
        else:
            # If there is a following section in the course, return the id of its first
            # lesson. Otherwise, we reached the final of the course
            next_lesson = Leccion.objects.filter(
                seccion__orden=lesson.seccion.orden+1,
                seccion__curso=lesson.seccion.curso,
                orden=1
            ).first()
            if next_lesson:
                return next_lesson.slug
            else:
                return lesson.slug
            
    elif direction == 'previous':
        # If there is a previous lesson in the section, return its id. Otherwise,
        # come back to the previous section.
        previous_lesson = Leccion.objects.filter(
            seccion=lesson.seccion,
            orden=lesson.orden-1
        ).first()
        if previous_lesson:
            return previous_lesson.slug
        else:
            # If there is a previous section in the course, return the id of its last
            # lesson. Otherwise, we reached the beginning of the course
            previous_lesson = Leccion.objects.filter(
                seccion__orden=lesson.seccion.orden-1,
                seccion__curso=lesson.seccion.curso
            ).order_by('-orden').first()
            if previous_lesson:
                return previous_lesson.slug
            else:
                return lesson.slug
            

def get_curso(course_slug):
    if course_slug == 'programa':
        return None
    return get_object_or_404(Curso, slug=course_slug, state=True)


def get_precio(curso):
    if curso:
        return str(curso.precio).replace(',', '.')
    return '30.00'