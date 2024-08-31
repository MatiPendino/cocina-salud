from .models import Movimiento

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