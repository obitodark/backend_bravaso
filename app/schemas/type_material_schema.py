from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.type_material_model import TypeMaterialModel


class TypeMaterialRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('Type_material Create', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })

    def update(self):
        return self.namespace.model('Type_material Update', {
            'name': fields.String(required=True, min_length=2, max_length=120)
        })


class TypeMaterialResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TypeMaterialModel
        ordered = True
    # product=Nested('ProductsResponseSchema',exclude=['type_materials'],many=True)