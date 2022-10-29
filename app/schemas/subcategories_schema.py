from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.sub_categories_model import SubCategoryModel


class SubcategoriesRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('subCategory Create', {
            'name': fields.String(required=True, min_length=2, max_length=120),
            'id_category':fields.Integer(required=True, min_length=2, max_length=3 )
        })

    def update(self):
        return self.namespace.model('subCategory Update', {
            'name': fields.String(required=False, min_length=2, max_length=120),
            'id_category':fields.Integer(required=False, min_length=2, max_length=3 )
        })


class SubcategoriesResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SubCategoryModel
        ordered = True
        include_fk=['id_category']
    products=Nested('ProductsResponseSchema',exclude=['subcategory'],many=True)
    category=Nested('CategoriesResponseSchema',exclude=['subcategory'],many=True)