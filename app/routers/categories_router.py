from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.categories_schema import CategoriesRequestSchema
from app.controllers.categories_controller import CategoriesController

namespace = api.namespace(
    name='Categories',
    description='Endpoints para las categorias de los productos',
    path='/categories'
)

schema = CategoriesRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Categories(Resource):
    # @jwt_required()
    def get(self):
        ''' Listar todas las categorias '''
        controller = CategoriesController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear una categoria '''
        controller = CategoriesController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class CategoryById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una categoria por el ID '''
        controller = CategoriesController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una categoria por el ID '''
        controller = CategoriesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una categoria por el ID '''
        controller = CategoriesController()
        return controller.delete(id)


api.add_namespace(namespace)
