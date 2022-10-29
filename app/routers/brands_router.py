from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.brands_schema import BrandsRequestSchema
from app.controllers.brands_controller import BrandsController

namespace = api.namespace(
    name='Brands',
    description='Endpoints para las marcas de los productos',
    path='/brands',
)

schema = BrandsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Brands(Resource):
    # @jwt_required()
    def get(self):
        ''' Listar todas las marcas '''
        controller = BrandsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear una marcas '''
        controller = BrandsController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class BrandsById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una marcas por el ID '''
        controller = BrandsController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una marcas por el ID '''
        controller = BrandsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una marcas por el ID '''
        controller = BrandsController()
        return controller.delete(id)


api.add_namespace(namespace)
