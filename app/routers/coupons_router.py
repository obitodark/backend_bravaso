from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.coupons_schema import CouponsRequestSchema
from app.controllers.coupons_controller import CouponsController

namespace = api.namespace(
    name='Coupons',
    description='Endpoints para las cupones',
    path='/coupons'
)

schema = CouponsRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Coupons(Resource):
    @jwt_required()
    def get(self):
        ''' Listar todas los cupones '''
        controller = CouponsController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear un cupon '''
        controller = CouponsController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class CouponById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un cupon por el ID '''
        controller = CouponsController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un cupon por el ID '''
        controller = CouponsController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un cupon por el ID '''
        controller = CouponsController()
        return controller.delete(id)


api.add_namespace(namespace)
