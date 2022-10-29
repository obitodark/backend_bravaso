from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.shopping_cart_model import ShoppingCartModel
from marshmallow.fields import Nested


class ShoppingCartsRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def update(self):
        return self.namespace.model('Shopping Cart Create', {
            'product_id': fields.Integer(required=True, min=1),
            'quantity': fields.Integer(required=True, min=1)
        })


class ShoppingCartsResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ShoppingCartModel
        ordered = True

    product = Nested('ProductsResponseSchema', many=False)
