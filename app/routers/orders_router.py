from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.controllers.orders_controller import OrderController

namespace = api.namespace(
    name='Orders',
    description='Endpoints para ordenes - pedidos',
    path='/orders'
)


@namespace.route('')
@namespace.doc(security='Bearer')
class Categories(Resource):
    @jwt_required()
    def post(self):
        ''' Crear un pedido '''
        controller = OrderController()
        return controller.create()
