from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.product_images_schema import ImagesProductRequestSchema
from app.controllers.product_images_controller import ProductImagesController

namespace = api.namespace(
    name='Productos -Images',
    description='Endpoints para las imagenes de productos',
    path='/product-images'
)

schema = ImagesProductRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class Categories(Resource):
    # @jwt_required()
    def get(self):
        ''' Listar todas las imagenes de produtos '''
        controller = ProductImagesController()
        return controller.all()

    # @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear un imgen para el producto '''
        controller = ProductImagesController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class CategoryById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una imagen de  product '''
        controller = ProductImagesController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una  imagen de  producto '''
        controller = ProductImagesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una  imagen de       producto '''
        controller = ProductImagesController()
        return controller.delete(id)


api.add_namespace(namespace)
