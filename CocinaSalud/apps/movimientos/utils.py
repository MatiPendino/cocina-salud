import string
import random
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.http import HttpResponse
from apps.usuario_custom.models import Usuario
from apps.curso.models import CursoUsuario, LeccionUsuario, Leccion
from apps.movimientos.models import Movimiento, MedioDePago
from apps.movimientos.implementations import impl_paypal

def generate_unique_code():
    characters = string.ascii_letters + string.digits
    unique_code = ''.join(random.choices(characters, k=13))    
    try:
        codigo_operacion = Movimiento.objects.get(codigo_operacion=unique_code)
        return generate_unique_code()
    except:
        return unique_code


def get_movimiento_condicion(request, movimiento):
    if movimiento.medio_de_pago.tipo == MedioDePago.TIPO_PAYPAL:
        condicion = impl_paypal.ipn(request, movimiento)
    
    return condicion


def create_curso_lecciones_usuario(user, curso):
    usuario = Usuario.objects.get(user=user, state=True)
    CursoUsuario.objects.create(
        curso=curso,
        usuario=usuario,
    )
    lecciones = Leccion.objects.filter(
        state=True,
        seccion__curso=curso
    )

    for leccion in lecciones:
        LeccionUsuario.objects.create(
            leccion=leccion,
            usuario=usuario
        )


def send_compra_via_email(email_buyer, course):
    message = f'''
        Muchas gracias por tu compra!
    '''
    print(email_buyer)
    print(course)

    '''send_mail(
        'Confirmación de compra',
        message,
        'cocinasalud2001@gmail.com',
        [email_buyer],
        fail_silently=False
    )'''

    html = '<h1>Mensaje importante</h1>'

    msg = EmailMultiAlternatives(
        'compra', 'important message', 'cocinasalud2001@gmail.com', [email_buyer]
    )
    msg.attach_alternative(html, "text/html")
    msg.send()

    print('Sobrevivimos')
    # return HttpResponse('Email sent successfully')