from app import api
from flask import request
from flask_restx import Resource
from app.schemas.mercadopago_schema import MercadoPagoRequestSchema
from app.utils.mercadopago import Mercadopago
from app.controllers.mercadopago_controller import MercadoPagoController

namespace = api.namespace(
    name='Mercadopago',
    description='Endpoints para la integración de mercadopago',
    path='/mercadopago'
)

schema = MercadoPagoRequestSchema(namespace)


@namespace.route('/users/test')
class UserTest(Resource):
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear un usuario de prueba '''
        util = Mercadopago()
        return util.createUserTest(request.json)


@namespace.route('/methods_paying')
class MethodsPaying(Resource):
    def get(self):
        ''' Listar todos los medios de pago '''
        util = Mercadopago()
        return util.allMethodsPaying()


@namespace.route('/preferences/create')
class Preferences(Resource):
    def post(self):
        ''' Crear url de pagos '''
        util = Mercadopago()
        return util.createPreferences()


@namespace.route('/webhook')
class Webhook(Resource):
    def post(self):
        ''' Webhook de pagos '''
        args = request.args.to_dict()
        payment_id = args['id']
        print(f'Se recibe pago {payment_id}')
        controller = MercadoPagoController()
        controller.updatePayment(payment_id)
        return {}, 200


api.add_namespace(namespace)
