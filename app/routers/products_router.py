from flask import request
from app import api

from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.products_schema import ProductsRequestSchema
from app.controllers.products_controller import ProductsController

namespace = api.namespace(
    name='Products',
    description='Endpoints para los productos',
    path='/products'
)

schema = ProductsRequestSchema(namespace)


@namespace.route('')

class Products(Resource):
    @namespace.doc(security='Bearer')
    # @jwt_required()
    def get(self):
        ''' Listar todos los productos '''
        controller = ProductsController()
        return controller.all()

   
  
    @namespace.expect(schema.create(),validate=True)
    @namespace.doc(security='Bearer')
    # @jwt_required()
    def post(self):
        ''' Crear un producto '''
        form = schema.create().parse_args()
        controller = ProductsController()
        return controller.create(form)


@namespace.route('/filter/<int:page>/<int:perpage>')
class ProductFilter(Resource):

# @namespace.route('/filter/<int:idc>/<int:ids>/<int:page>/<int:per_page>/<int:id_brands>/')
# @namespace.doc(security='Bearer')
# class ProductById(Resource):
    # @jwt_required()
    @namespace.expect(schema.filterProduct(),validate=True)
    def post(self,page,perpage):
        ''' Obtener un producto por filtro'''
      
        controller = ProductsController()
        return controller.filterByCategory( page,perpage,request.json)





@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class ProductById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener un producto por el ID '''
        controller = ProductsController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar un producto por el ID '''
        form = schema.update().parse_args()
        controller = ProductsController()
        return controller.update(id, form)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar un producto por el ID '''
        controller = ProductsController()
        return controller.delete(id)


api.add_namespace(namespace)
