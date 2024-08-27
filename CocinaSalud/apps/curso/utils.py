from django.shortcuts import get_object_or_404
from apps.curso.models import Leccion, LeccionUsuario, CursoUsuario, Curso
from apps.movimientos.models import Movimiento, MedioDePago


def get_percentage_rating(rating, num_ratings):
    return round(rating / num_ratings * 100, 2) if num_ratings > 0 else 0


def get_lessons_for_section(lecciones_usuario, seccion):
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


def update_last_seen_user_lesson(instance):
    # Remove the "last" check in the previous seen user lesson
    last_seen_user_lesson = LeccionUsuario.objects.filter(
        usuario__user=instance.request.user,
        leccion__seccion__curso=instance.object.seccion.curso,
        ultima=True
    ).first()
    if last_seen_user_lesson:
        last_seen_user_lesson.ultima = False
        last_seen_user_lesson.save()

    # Add the "last" check in the current user lesson
    current_user_lesson = LeccionUsuario.objects.filter(
        usuario__user=instance.request.user,
        leccion=instance.object,
        state=True
    ).first()
    current_user_lesson.ultima = True
    current_user_lesson.save()


def leave_review(curso_usuario_id, rating, comment):
    # If the user leaves a review, will update curso_usuario object 
    # and course average qualification
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
    average_calification = sum_stars / len(cursos_usuarios)
    curso.calificacion = average_calification
    curso.save()


def complete_lesson(lesson_slug, user):
    user_lesson = LeccionUsuario.objects.filter(
        usuario__user=user,
        leccion__slug=lesson_slug
    ).first()
    user_lesson.completada = True
    user_lesson.save()


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

def create_movimiento(curso, usuario, paypal_mdp, codigo_operacion):
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