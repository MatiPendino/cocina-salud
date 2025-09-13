from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.usuario_custom.models import Usuario
from apps.curso.models import Curso, CursoUsuario, Leccion, Seccion, LeccionUsuario
from apps.curso.services import (
    get_estrellas, get_secciones_lecciones_usuario, update_last_seen_leccion_usuario,
    dejar_resenia
)

User = get_user_model()

class ServicesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing', password='testing123')
        self.usuario = Usuario.objects.create(user=self.user)
        self.curso = Curso.objects.create(
            nombre='curso test',
            precio=10,
            descripcion_breve='curso de prueba',
            num_alumnos=2,
            num_calificaciones=2,
            calificacion=3
        )
        self.curso_usuario1 = CursoUsuario.objects.create(
            curso=self.curso,
            usuario=self.usuario,
            calificacion=2
        )
        self.curso_usuario2 = CursoUsuario.objects.create(
            curso=self.curso,
            usuario=self.usuario,
            calificacion=4
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

    def test_get_estrellas(self):
        cursos_usuarios = CursoUsuario.objects.all()
        estrellas = get_estrellas(cursos_usuarios)
        self.assertEqual(estrellas['num_total_estrellas'], 2)

        suma_cantidad_estrellas = sum([estrellas['una_estrella'], estrellas['dos_estrellas'], 
            estrellas['tres_estrellas'], estrellas['cuatro_estrellas'], 
            estrellas['cinco_estrellas']
        ])
        self.assertEqual(estrellas['num_total_estrellas'], suma_cantidad_estrellas)

        suma_porcentajes = sum([estrellas['una_estrella_p'], estrellas['dos_estrellas_p'],
            estrellas['tres_estrellas_p'], estrellas['cuatro_estrellas_p'], 
            estrellas['cinco_estrellas_p']                  
        ])
        self.assertEqual(suma_porcentajes, 100)

    
    def test_get_secciones_lecciones_usuario(self):
        secciones_lecciones_usuario_func = get_secciones_lecciones_usuario(self.user, self.curso)
        secciones_lecciones_usuario_dict = {
            'seccion1': [self.leccion_usuario1],
            'seccion2': [self.leccion_usuario2]
        }
        self.assertEqual(secciones_lecciones_usuario_func, secciones_lecciones_usuario_dict)


    def test_update_last_seen_leccion_usuario(self):
        update_last_seen_leccion_usuario(self.user, self.leccion2)
        self.leccion_usuario1.refresh_from_db()
        self.leccion_usuario2.refresh_from_db()

        self.assertFalse(self.leccion_usuario1.ultima)
        self.assertTrue(self.leccion_usuario2.ultima)


    def test_dejar_resenia(self):
        curso_usuario3 = CursoUsuario.objects.create(
            curso=self.curso,
            usuario=self.usuario,
        )
        
        calificacion_curso_usuario = 2
        opinion_curso_usuario = 'muy buen curso'
        dejar_resenia(curso_usuario3.id, calificacion_curso_usuario, opinion_curso_usuario)
        curso_usuario3.refresh_from_db()
        self.curso.refresh_from_db()

        self.assertEqual(curso_usuario3.calificacion, calificacion_curso_usuario)
        self.assertEqual(curso_usuario3.opinion, opinion_curso_usuario)

        promedio_curso = round(
        (self.curso_usuario1.calificacion + self.curso_usuario2.calificacion + curso_usuario3.calificacion) 
        / self.curso.get_cantidad_cursos_usuarios(), 2
        )
        self.assertEqual(self.curso.calificacion, promedio_curso)