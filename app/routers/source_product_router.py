from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.source_product_schema import Source_ProductRequestSchema
from app.controllers.source_product_controller import SourceProductController

namespace = api.namespace(
    name='SourceProduct',
    description='Endpoints para las origen de los productos',
    path='/source-products'
)

schema = Source_ProductRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class SourceProduct(Resource):
    
    def get(self):
        ''' Listar todas las origen '''
        controller = SourceProductController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear una origen'''
        controller = SourceProductController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class SourceProductById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una origen por el ID '''
        controller = SourceProductController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una origen por el ID '''
        controller = SourceProductController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una origen por el ID '''
        controller = SourceProductController()
        return controller.delete(id)


api.add_namespace(namespace)
