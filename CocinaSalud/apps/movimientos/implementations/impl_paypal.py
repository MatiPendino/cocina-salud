import requests
import json
import base64
from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment, LiveEnvironment 
from paypalcheckoutsdk.orders import OrdersGetRequest, OrdersCaptureRequest
from apps.movimientos.models import Movimiento

def paypal_token(cliente_id, client_secret):
    url = "https://api-m.sandbox.paypal.com/v1/oauth2/token"
    data = {
                "client_id": cliente_id,
                "client_secret": client_secret,
                "grant_type":"client_credentials"
            }
    headers = {
                "Content-Type": "application/x-www-form-urlencoded",
                "Authorization": "Basic {0}".format(base64.b64encode((cliente_id + ":" + client_secret).encode()).decode())
            }

    token = requests.post(url, data, headers=headers)
    return token.json()['access_token']


class PayPalClient:
    def __init__(self, movimiento):
        self.client_id = movimiento.medio_de_pago.client_id
        self.client_secret = movimiento.medio_de_pago.secret_key
        if movimiento.medio_de_pago.test:
            self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        else:
            self.environment = LiveEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)


class GetOrder(PayPalClient):
    def get_order(self, order_id):
        request = OrdersGetRequest(order_id)
        response = self.client.execute(request)
        return response


class CaptureOrder(PayPalClient):
    def capture_order(self, order_id, debug=False):
        request = OrdersCaptureRequest(order_id)
        response = self.client.execute(request)
        if debug:
            print ('Status Code: ', response.status_code)
            print ('Status: ', response.result.purchase_units[0].payments.captures[0].status)
            print ('Order ID: ', response.result.id)
            print ('Links: ')
        return response
    

def ipn(request, movimiento):
    data = json.loads(request.body)
    order_id = data['orderID']
    
    detalle = GetOrder(movimiento).get_order(order_id)
    detalle_precio = float(detalle.result.purchase_units[0].amount.value)

    if float(detalle_precio) == float(movimiento.importe):
        transaccion = CaptureOrder(movimiento).capture_order(order_id, debug=False)

        # if transaccion.status_code in [200, 201] and transaccion.result.status in ['APPROVED', 'COMPLETED']:
        if transaccion.status_code in [200, 201] and transaccion.result.purchase_units[0].payments.captures[0].status in ['APPROVED', 'COMPLETED']:
            print(f'''
                PAGO REALIZADO CON ÉXITO:
                Código operación: {transaccion.result.purchase_units[0].reference_id}
                Status Code:, {transaccion.status_code}
                Status: {transaccion.result.status}
                Order ID:, {transaccion.result.id}
                '''
            )
            return Movimiento.ESTADO_FINALIZADA
        else:
            print(f'''
                ERROR AL COMPLETAR EL PAGO
                Código operación: {transaccion.result.purchase_units[0].reference_id}
                Status Code: {transaccion.status_code}
                Status: {transaccion.result.status}
                Order ID: {transaccion.result.id}
                '''
            )
            return Movimiento.ESTADO_NO_FINALIZADA
    else:
        print(f'''
            Código operación: {movimiento.codigo_operacion}
            Precios incorrectos:
            '''
        )
        return Movimiento.ESTADO_NO_FINALIZADA
    

