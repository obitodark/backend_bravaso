from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.categories__model import CategoryModel


class CategoriesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Category Create', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })

    def update(self):
        return self.namespace.model('Category Update', {
            'name': fields.String(required=True, min_length=2, max_length=120),
             
        })


class CategoriesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = CategoryModel
        ordered = True

    product=Nested('ProductsResponseSchema',exclude=['category'],many=True)   
    # subcategory=Nested('SubcategoriesResponseSchema',exclude=['category'],many=True)