
from flask_restx import fields
from marshmallow.fields import Nested
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.image_user_model import ImagesUserModel


class ImagesUserRequestSchema:
    def __init__(self, namespace):
        self.namespace = namespace

    def create(self):
        return self.namespace.model('user-images Create', {
            'image_id': fields.Integer(required=True, min_length=1, max_length=120),
             'user_id': fields.Integer(required=True, min_length=1, max_length=20)
        })

    def update(self):
        return self.namespace.model('user-images Update', {
            'image_id': fields.Integer(required=True, min_length=1, max_length=120),
             'user_id': fields.Integer(required=True, min_length=1, max_length=20)
        })


class ImagesUserResponseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = ImagesUserModel
        ordered = True
        
        
          
    images=Nested('ImagesResponseSchema',uselist=False,exclude=['imagesUser'],back_populates='imagesUser') 
    user=Nested('UsersResponseSchema',uselist=False,exclude=['imagesUser'],back_populates='imagesUser')