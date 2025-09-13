from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.usuario_custom.models import Usuario
from apps.curso.models import CursoUsuario, LeccionUsuario, Leccion, Curso, Seccion
from apps.curso.selectors import (
    get_cursos_usuarios_calificacion,
    get_curso_usuario,
    get_leccion_usuario,
    get_lecciones_usuario,
    get_leccion_usuario_actual,
    get_leccion_usuario_last_seen,
    get_primera_leccion
)

User = get_user_model()

class SelectorsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing', password='testing123')
        self.usuario = Usuario.objects.create(user=self.user)
        self.curso = Curso.objects.create(
            nombre='curso1',
            precio=10,
            slug='curso1',
            descripcion_breve='curso de test',
        )
        self.seccion = Seccion.objects.create(
            nombre='seccion1',
            curso=self.curso,
            orden=1
        )
        self.leccion = Leccion.objects.create(
            nombre='leccion1',
            seccion=self.seccion,
            orden=1
        )
        self.curso_usuario = CursoUsuario.objects.create(
            curso=self.curso,
            usuario=self.usuario
        )
        self.leccion_usuario = LeccionUsuario.objects.create(
            leccion=self.leccion,
            usuario=self.usuario
        )

    def test_get_cursos_usuarios_calificacion_sin_calificacion(self):
        """
        Debe devolver únicamente las instancia de CursoUsuario que hayan calificado el curso
        """
        cursos_usuarios = get_cursos_usuarios_calificacion(self.curso)
        self.assertEqual(cursos_usuarios.count(), 0)


    def test_get_cursos_usuarios_calificacion_con_calificacion(self):
        """
        Debe devolver únicamente las instancia de CursoUsuario que hayan calificado el curso
        """
        curso_usuario2 = CursoUsuario.objects.create(
            curso=self.curso,
            usuario=self.usuario,
            calificacion=1
        )
        cursos_usuarios = get_cursos_usuarios_calificacion(self.curso)
        self.assertEqual(cursos_usuarios.count(), 1)


    def test_get_curso_usuario(self):
        curso_usuario = get_curso_usuario(self.curso.id, self.user)
        self.assertIsNotNone(curso_usuario)


    def test_get_leccion_usuario(self):
        leccion_usuario = get_leccion_usuario(self.leccion.slug, self.user)
        self.assertIsNotNone(leccion_usuario)

    
    def test_get_lecciones_usuario(self):
        lecciones_usuario = get_lecciones_usuario(self.user, self.curso)
        self.assertEqual(lecciones_usuario.count(), 1)


    def test_get_leccion_usuario_actual(self):
        leccion_usuario_actual = get_leccion_usuario_actual(self.user, self.leccion)
        self.assertIsNotNone(leccion_usuario_actual)


    def test_get_leccion_usuario_last_seen_no_ultimo(self):
        leccion_usuario = get_leccion_usuario_last_seen(self.user, self.curso.slug)
        self.assertIsNone(leccion_usuario)


    def test_get_leccion_usuario_last_seen_ultimo(self):
        """Si tenemos una lección marcada como última, debe devolverla"""
        leccion_usuario_ultimo = LeccionUsuario.objects.create(
            leccion=self.leccion,
            usuario=self.usuario,
            ultima=True
        )
        self.assertIsNotNone(get_leccion_usuario_last_seen(self.user, self.curso.slug))


    def test_primera_leccion_no_primera(self):
        """Si el curso no tiene una lección marcada como primera, debe lanzar una excepción"""
        curso2 = Curso.objects.create(
            nombre='curso2',
            precio=10,
            slug='curso2',
            descripcion_breve='curso de test',
        )
        seccion2 = Seccion.objects.create(
            nombre='seccion2',
            curso=curso2,
            orden=2
        )
        leccion2 = Leccion.objects.create(
            nombre='leccion2',
            seccion=seccion2,
            orden=2
        )
        with self.assertRaises(Leccion.DoesNotExist):
            get_primera_leccion(curso2.slug)

    
    def test_primera_leccion_primera(self):
        leccion = get_primera_leccion(self.curso.slug)
        self.assertIsNotNone(leccion)