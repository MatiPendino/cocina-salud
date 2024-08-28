from apps.curso.models import CursoUsuario, LeccionUsuario, Leccion

def get_cursos_usuarios_curso(curso):
    cursos_usuarios = CursoUsuario.objects.filter(
        curso=curso, 
        state=True, 
        calificacion__gte=1
    )
    return cursos_usuarios


def get_curso_usuario(curso_id, user):
    curso_usuario = CursoUsuario.objects.filter(
        curso__id=curso_id,
        usuario__user=user
    ).first()
    return curso_usuario


def get_lecciones_usuario(user, curso):
    lecciones_usuario = LeccionUsuario.objects.filter(
        usuario__user=user, 
        leccion__seccion__curso=curso, 
        state=True
    )
    return lecciones_usuario

def get_current_user_lesson(user, leccion):
    current_user_lesson = LeccionUsuario.objects.filter(
        usuario__user=user,
        leccion=leccion
    ).first()
    return current_user_lesson

def get_last_seen_leccion_usuario(user, curso_slug):
    last_seen_leccion_usuario = LeccionUsuario.objects.filter(
        usuario__user=user,
        leccion__seccion__curso__slug=curso_slug,
        ultima=True,
        state=True
    ).first()
    return last_seen_leccion_usuario

def get_primera_leccion(curso_slug):
    primera_leccion = Leccion.objects.get(
        Leccion,
        seccion__curso__slug=curso_slug,
        seccion__orden=1,
        orden=1,
        state=True
    )
    return primera_leccion