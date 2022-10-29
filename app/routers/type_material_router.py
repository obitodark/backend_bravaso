from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.type_material_schema import TypeMaterialRequestSchema
from app.controllers.type_material_controller import TypeMaterialController

namespace = api.namespace(
    name='Type_Material',
    description='Endpoints para las tipo  de material de los productos',
    path='/type_material'
)

schema =TypeMaterialRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class SourceProduct(Resource):
    
    def get(self):
        ''' Listar todas lo tipos material de producto '''
        controller = TypeMaterialController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear un type material de producto'''
        controller = TypeMaterialController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class SourceProductById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una tipo de material  por el ID '''
        controller = TypeMaterialController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar el tipo de material por el ID '''
        controller = TypeMaterialController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar el tipo material por el ID '''
        controller = TypeMaterialController()
        return controller.delete(id)


api.add_namespace(namespace)
