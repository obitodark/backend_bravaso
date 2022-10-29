from sqlalchemy import desc
from app import db
from app.models.image_user_model import ImagesUserModel
from app.schemas.user_images_schema import ImagesUserResponseSchema
from app.utils.bucket import Bucket


class UsersImagesController:
    def __init__(self):
        self.model = ImagesUserModel
        self.schema = ImagesUserResponseSchema
       
        # self.data1=self.model.where(category_id=data['id_category'],subcategory_id=data['id_subcategory']).order_by('id').paginate(
        #                 per_page=data['per_page'], page=data['page'] )


    def all(self):
        try:
            records = self.model.where(status=True).order_by('id').all()
            response = self.schema(many=True)
            return {
                'data': response.dump(records)
            }
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def getById(self, id):
        try:
            if record := self.model.where(id=id).first():
                response = self.schema(many=False)
                return {
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro la avatar usuario'
            }, 404
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def create(self, data):
        try:
            new_record = self.model.create(**data)
            db.session.add(new_record)
            db.session.commit()

            response = self.schema(many=False)

            return {
                'messsage': 'avatar usuario se creo con exito',
                'data': response.dump(new_record)
            }, 201
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def update(self, id, data):
        try:
            if record := self.model.where(id=id).first():
                record.update(**data)
                db.session.add(record)
                db.session.commit()

                response = self.schema(many=False)
                return {
                    'messsage': 'avatar usuario se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro avatar usuario mencionada'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def delete(self, id):
        try:
            if record := self.model.where(id=id).first():
                if record.status:
                    record.update(status=False)
                    db.session.add(record)
                    db.session.commit()
                return {
                    'message': 'Se deshabilito avatar usuario con exito'
                }, 200
            return {
                'message': 'No se encontro avatar usuario mencionada'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
