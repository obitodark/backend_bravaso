from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.stores_locations_schema import StoresLocationsRequestSchema
from app.controllers.stores_locations_controller import StoresLocationsController

namespace = api.namespace(
    name='Stores Locations',
    description='Endpoints para la localidad de las tiendas',
    path='/stores_locations'
)

schema = StoresLocationsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class StoresLocations(Resource):
    @jwt_required()
    def get(self):
        ''' Listar todas las localidades '''
        controller = StoresLocationsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear una localidad '''
        controller = StoresLocationsController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class StoreLocationById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una localidad por el ID '''
        controller = StoresLocationsController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una localidad por el ID '''
        controller = StoresLocationsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una localidad por el ID '''
        controller = StoresLocationsController()
        return controller.delete(id)


api.add_namespace(namespace)
