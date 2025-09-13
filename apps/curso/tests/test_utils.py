from django.test import TestCase
from django.contrib.auth import get_user_model
from django.http import Http404
from apps.usuario_custom.models import Usuario
from apps.curso.models import Curso, Seccion, Leccion, LeccionUsuario
from apps.curso.utils import (
    get_porcentaje_estrella, get_curso, get_precio_str, get_leccion_usuario_por_seccion
)

User = get_user_model()
class UtilsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing', password='testing123')
        self.usuario = Usuario.objects.create(user=self.user)
        self.curso = Curso.objects.create(
            nombre='curso test',
            precio=10,
            descripcion_breve='curso de prueba',
        )
        self.seccion1 = Seccion.objects.create(
            nombre='seccion1',
            curso=self.curso,
            orden=1
        )
        self.seccion2 = Seccion.objects.create(
            nombre='seccion2',
            curso=self.curso,
            orden=1
        )
        self.leccion1 = Leccion.objects.create(
            nombre='leccion1',
            seccion=self.seccion1,
            orden=1
        )
        self.leccion2 = Leccion.objects.create(
            nombre='leccion2',
            seccion=self.seccion2,
            orden=1
        )
        self.leccion_usuario1 = LeccionUsuario.objects.create(
            leccion=self.leccion1,
            usuario=self.usuario,
            ultima=True
        )
        self.leccion_usuario2 = LeccionUsuario.objects.create(
            leccion=self.leccion2,
            usuario=self.usuario
        )

    def test_get_porcentaje_estrella(self):
        self.assertEqual(get_porcentaje_estrella(3, 9), 33.33)
        self.assertEqual(get_porcentaje_estrella(0, 0), 0)
        self.assertEqual(get_porcentaje_estrella(4, 0), 0)
        self.assertEqual(get_porcentaje_estrella(1, -1), 0)


    def test_get_precio(self):
        self.assertEqual(get_precio_str(self.curso), '10')
        self.assertEqual(get_precio_str(None), '30.00')


    def test_get_curso(self):
        self.assertIsNone(get_curso('programa'))
        self.assertEqual(get_curso(self.curso.slug), self.curso)
        with self.assertRaises(Http404):
            get_curso('slug no existente')


    def test_get_leccion_usuario_por_seccion(self):
        lecciones_usuario = LeccionUsuario.objects.all()
        lecciones_usuario_por_seccion = get_leccion_usuario_por_seccion(
            lecciones_usuario, self.seccion1
        )
        lecciones_usuario_por_seccion_list = [self.leccion_usuario1]
        self.assertEqual(lecciones_usuario_por_seccion, lecciones_usuario_por_seccion_list)