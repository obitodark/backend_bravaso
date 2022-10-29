from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.products_model import ProductsModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class ProductsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace


    def filterProduct(self):
        return self.namespace.model('filter product', {
            'id_category': fields.Integer(required=True, min_length=1, max_length=5),
             'id_subcategory': fields.Integer(required=True, min_length=1, max_length=5),
              'id_brands': fields.Integer(required=True, min_length=1, max_length=5),
              'price': fields.Integer(required=True, min_length=1, max_length=5),
              'search': fields.String(required=False),
            #    'page': fields.Integer(required=True, min_length=1, max_length=5),
            #     'per_page': fields.Integer(required=True, min_length=1, max_length=5)
        })    

    def create(self):
        parser = RequestParser()
        parser.add_argument('name', type=str, required=True, location='form')
        parser.add_argument('description', type=str,
                            required=True, location='form')
        parser.add_argument('price', type=float,
                            required=True, location='form')
       
        parser.add_argument('stock', type=int, required=True, location='form')
        parser.add_argument('category_id', type=int,
                            required=True, location='form')
        parser.add_argument('subcategory_id', type=int,
                            required=True, location='form')                     

        parser.add_argument('weight', type=float,
                            required=False, location='form')               
        parser.add_argument('brand_id', type=int, required=True, location='form')                     
        parser.add_argument('source_id', type=int, required=True, location='form')  
        parser.add_argument('type_material_id', type=int, required=True, location='form')  
      
    
        return parser

    def update(self):
        parser = RequestParser()
        parser.add_argument('name', type=str, required=False, location='form')
        parser.add_argument('description', type=str,
                            required=False, location='form')
        parser.add_argument('price', type=float,
                            required=False, location='form')
    

        parser.add_argument('stock', type=int, required=False, location='form')
        parser.add_argument('category_id', type=int,
                            required=False, location='form')
        parser.add_argument('subcategory_id', type=int,
                            required=False, location='form')   
                                             
        parser.add_argument('weight', type=float,
                            required=False, location='form')               
        parser.add_argument('brand_id', type=int, required=False, location='form')                     
        parser.add_argument('source_id', type=int, required=False, location='form') 
        parser.add_argument('type_material_id', type=int, required=False, location='form')                     
                    

        return parser


class ProductsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ProductsModel
        ordered = True
    subcategory=Nested('SubcategoriesResponseSchema',exclude=['products'],many=False)
    category=Nested('CategoriesResponseSchema',exclude=['product'],many=False)
    brand=Nested('BrandsResponseSchema',exclude=['products'],many=False)
    source_products=Nested('Source_ProductResponseSchema',exclude=['product'],many=False)    
    images=Nested('ImagesProductResponseSchema',exclude=['product','status'],many=True)
    type_materials=Nested('TypeMaterialResponseSchema',many=True) 