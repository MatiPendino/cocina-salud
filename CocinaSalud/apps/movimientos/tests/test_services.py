from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.movimientos.utils import generate_unique_code
from apps.usuario_custom.models import Usuario
from apps.curso.models import Curso, CursoUsuario, Seccion, Leccion, LeccionUsuario
from apps.movimientos.models import MedioDePago
from apps.movimientos.services import (
    create_movimiento, finalizar_compra, create_curso_lecciones_usuario
)

User = get_user_model()
class ServicesTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testing', password='testing123')
        self.usuario = Usuario.objects.create(user=self.user)
        self.curso = Curso.objects.create(
            nombre='curso test',
            precio=10,
            descripcion_breve='curso de prueba'
        )
        self.medio_de_pago = MedioDePago.objects.create(
            nombre='PayPal mdp',
            tipo=MedioDePago.TIPO_PAYPAL,
            client_id='client_id',
            secret_key='secret_key',
            moneda_codigo='USD',
            test=False
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

    def test_create_movimiento_curso(self):
        codigo_operacion = generate_unique_code()
        movimiento = create_movimiento(
            self.curso, self.usuario, self.medio_de_pago, codigo_operacion
        )
        self.assertEqual(movimiento.curso, self.curso)

    def test_create_movimiento_programa(self):
        codigo_operacion = generate_unique_code()
        movimiento = create_movimiento(
            None, self.usuario, self.medio_de_pago, codigo_operacion
        )
        self.assertIsNone(movimiento.curso)


    def test_create_curso_lecciones_usuario(self):
        create_curso_lecciones_usuario(self.user, self.curso)
        self.assertIsNotNone(CursoUsuario.objects.all())
        self.assertIsNotNone(LeccionUsuario.objects.all())


    def test_finalizar_compra_curso(self):
        codigo_operacion = generate_unique_code()
        movimiento = create_movimiento(
            self.curso, self.usuario, self.medio_de_pago, codigo_operacion
        )
        finalizar_compra(self.user, movimiento)
        self.curso.refresh_from_db()

        self.assertEqual(self.curso.num_alumnos, 1)

    def test_finalizar_compra_programa(self):
        codigo_operacion = generate_unique_code()
        movimiento = create_movimiento(
            None, self.usuario, self.medio_de_pago, codigo_operacion
        )
        finalizar_compra(self.user, movimiento)
        self.usuario.refresh_from_db()

        self.assertTrue(self.usuario.compro_gestoria)