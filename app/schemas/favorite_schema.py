from flask_restx import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.favourite_model import FavoriteModel
from marshmallow.fields import Nested

class FavoriteResquestSchema:
    def __init__(self,namaspace):
        self.namaspace = namaspace

    def create(self):
        return self.namaspace.model('favorite create',{
            'product_id': fields.Integer(required=True, min=1)
        })    

class FavoriteResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model=FavoriteModel
        ordered = True        

    product = Nested('ProductsResponseSchema', many=False)    