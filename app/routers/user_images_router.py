from app import api
from flask import request
from flask_restx import Resource
from flask_jwt_extended import jwt_required
from app.schemas.user_images_schema import ImagesUserRequestSchema
from app.controllers.users_images_controller import UsersImagesController

namespace = api.namespace(
    name='users -Images',
    description='Endpoints  de avatar de usuario',
    path='/users-images'
)

schema = ImagesUserRequestSchema(namespace)


@namespace.route('')
@namespace.doc(security='Bearer')
class UserImages(Resource):
    # @jwt_required()
    def get(self):
        ''' Listar todas las avatar de usuarios '''
        controller = UsersImagesController()
        return controller.all()

    # @jwt_required()
    @namespace.expect(schema.create(), validate=True)
    def post(self):
        ''' Crear unavatar de usuarios '''
        controller = UsersImagesController()
        return controller.create(request.json)


@namespace.route('/<int:id>')
@namespace.doc(security='Bearer')
class UserImagesById(Resource):
    @jwt_required()
    def get(self, id):
        ''' Obtener una avatar de usuarios '''
        controller = UsersImagesController()
        return controller.getById(id)

    @jwt_required()
    @namespace.expect(schema.update(), validate=True)
    def put(self, id):
        ''' Actualizar una  avatar de usuarios '''
        controller = UsersImagesController()
        return controller.update(id, request.json)

    @jwt_required()
    def delete(self, id):
        ''' Deshabilitar una  avatar de usuarios '''
        controller = UsersImagesController()
        return controller.delete(id)


api.add_namespace(namespace)
