from flask import request
from app import api

from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.images_schema import ImagesRequestSchema
from app.controllers.images_controller import ImagesController

namespace = api.namespace(
    name='Images',
    description='Endpoints para los images',
    path='/images'
)

schema = ImagesRequestSchema(namespace)


@namespace.route('')

class Images(Resource):
    @namespace.doc(security='Bearer')
    # @jwt_required()
    def get(self):
        ''' Listar todos los imagenes '''
        controller = ImagesController()
        return controller.all()

   
  

  
    
    # @namespace.expect(schema.create(),validate=True)
    # @namespace.doc(security='Bearer')
    # # @jwt_required()
    # def post(self):
    #     ''' Crear imagen '''
    #     form = schema.create().parse_args()
    #     controller = ImagesController()
    #     return controller.create(form)



@namespace.route('/<string:nombre>')
class ImagesByIdCreate(Resource):
       @namespace.expect(schema.create(),validate=True)
       def post(self,nombre):
        ''' Crear imagen por id '''
        form = schema.create().parse_args()
        controller = ImagesController()
        return controller.createById(nombre,form)



@namespace.route('/<int:id>')
# @namespace.doc(security='Bearer')
class ImagesById(Resource):
    # @jwt_required()
  

    def get(self, id):
        ''' Obtener un producto por el ID '''
        controller =ImagesController()
        return controller.getById(id)

    # @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un imagen por el ID '''
        form = schema.update().parse_args()
        controller =ImagesController()
        return controller.update(id, form)

    # @jwt_required()
    def delete(self, id):
        ''' Deshabilitar imagen  por el ID '''
        controller =ImagesController()
        return controller.delete(id)
    # @namespace.route('/<int:id>')
    # @namespace.expect(schema.create(),validate=True)
    # def post(self,id):
    #     ''' Crear un producto '''
    #     form = schema.create().parse_args()
    #     controller = ImagesController()
    #     return controller.create(id,form)    


api.add_namespace(namespace)
