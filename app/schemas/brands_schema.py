
from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.brands_model import BrandsModel


class BrandsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Brands Create', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })

    def update(self):
        return self.namespace.model('Brands Update', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })


class BrandsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = BrandsModel
        ordered = True
    
    products=Nested('ProductsResponseSchema',exclude=['brand'],many=True)