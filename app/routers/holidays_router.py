from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.holidays_schema import HolidaysRequestSchema
from app.controllers.holidays_controller import HolidaysController

namespace = api.namespace(
    name='Holiday',
    description='Endpoints para los dias feriados',
    path='/holiday'
)

schema = HolidaysRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Holidays(Resource):
    @jwt_required()
    def get(self):
        ''' Listar todas los feriados '''
        controller = HolidaysController()
        return controller.all()

    @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear un feriado '''
        controller = HolidaysController()
        return controller.create(request.json)


@namespace.route('/delivery_dates')
@namespace.doc(security='Bearer')
class HolidaysDeliveryDates(Resource):
    # @jwt_required()
    def get(self):
        ''' Listar los dias de entrega '''
        controller = HolidaysController()
        return controller.deliveryDates()


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class HolidayById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un feriado por el ID '''
        controller = HolidaysController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un feriado por el ID '''
        controller = HolidaysController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un feriado por el ID '''
        controller = HolidaysController()
        return controller.delete(id)


api.add_namespace(namespace)
