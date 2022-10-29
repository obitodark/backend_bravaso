
from xml.etree.ElementInclude import include
from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.image_product_model import ImagesProductModel


class ImagesProductRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('product-images Create', {
            'image_id': fields.Integer(required=True, min_length=1, max_length=120),
             'product_id': fields.Integer(required=True, min_length=1, max_length=120)
        })

    def update(self):
        return self.namespace.model('product-images Update', {
            'image_id': fields.Integer(required=True, min_length=1, max_length=120),
             'product_id': fields.Integer(required=True, min_length=1, max_length=120)
        })


class ImagesProductResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ImagesProductModel
        ordered = True
        # include_fk=['product_id']
        # include_pk=[id]
        
    
    product=Nested('ProductsResponseSchema',exclude=['images'],include=['id'],many=False,back_populates='images')
    images=Nested('ImagesResponseSchema',uselist=False,exclude=['imagesProduct'],back_populates='imagesProduct') 