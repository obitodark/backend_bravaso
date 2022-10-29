from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.source_products_model import SourceProductModel


class Source_ProductRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Origen-producto Create', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })

    def update(self):
        return self.namespace.model('Origen-producto Update', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })


class Source_ProductResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SourceProductModel
        ordered = True
    product=Nested('ProductsResponseSchema',exclude=['source_products'],many=True)