from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.shopping_carts_schema import ShoppingCartsRequestSchema
from app.controllers.shopping_carts_controller import ShoppingCartsController

namespace = api.namespace(
    name='Shopping Carts',
    description='Endpoints para traer el carrito de compras',
    path='/shopping_carts'
)

schema = ShoppingCartsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class ShoppingCarts(Resource):
    @jwt_required()
    def get(self):
        ''' Listar productos del carrito '''
        controller = ShoppingCartsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self):
        ''' Crear o actualizar producto del carrito '''
        controller = ShoppingCartsController()
        return controller.update(request.json)


@namespace.route('/<int:product_id>')
@namespace.doc(security='Bearer')
class ShoppingCartById(Resource):
    @jwt_required()
    def delete(self, product_id):
        ''' Eliminar producto del carrito '''
        controller = ShoppingCartsController()
        return controller.delete(product_id)


api.add_namespace(namespace)
