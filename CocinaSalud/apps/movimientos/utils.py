import string
import random
from django.core.mail import EmailMultiAlternatives
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


def send_compra_via_email(email_buyer, course):
    message = f'''
        Muchas gracias por tu compra!
    '''

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


def get_slug_compra(curso):
    return curso.slug if curso else 'programa'