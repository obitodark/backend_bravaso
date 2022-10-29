from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.favorite_schema import FavoriteResquestSchema
from app.controllers.favorite_controller import FavouriteController

namespace = api.namespace(
    name='Favorite Products',
    description='Endpoints para traer productos favaritos',
    path='/favorite'
)

schema = FavoriteResquestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Favorite(Resource):
    @jwt_required()
    def get(self):
        ''' Listar productos del favritos '''
        controller = FavouriteController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear producto favorito '''
        controller = FavouriteController()
        return controller.create(request.json)


@namespace.route('/<int:product_id>')
@namespace.doc(security='Bearer')
class FavoriteById(Resource):
    @jwt_required()
    def delete(self, product_id):
        ''' Eliminar producto favorito '''
        controller = FavouriteController()
        return controller.delete(product_id)


api.add_namespace(namespace)


