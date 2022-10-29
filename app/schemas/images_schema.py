from xml.etree.ElementInclude import include
from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.image_model import ImagesModel
from flask_restx.reqparse import RequestParser
from werkzeug.datastructures import FileStorage


class ImagesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace


  

    def create(self):
        parser = RequestParser()
       
        parser.add_argument('image', type=FileStorage,
                            required=False, location='files')
       
        # parser.add_argument('product_id', type=int, required=True, location='form')
        return parser

    def update(self):
        parser = RequestParser()
        parser.add_argument('image', type=FileStorage,
                            required=True, location='files')
        # parser.add_argument('id_product', type=int, required=True, location='form')                    
        

        return parser


class ImagesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ImagesModel
        
        # ordered = True
        # include
    imagesProduct=Nested('ImagesProductResponseSchema',many=True,exclude=['images'],back_populates='images')
    imagesUser=Nested('ImagesUserResponseSchema',many=True,exclude=['images'],back_populates='images')
    