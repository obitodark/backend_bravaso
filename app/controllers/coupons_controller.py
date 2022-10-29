from app import db
from app.models.coupons_model import CouponModel
from app.schemas.coupons_schema import CouponsResponseSchema


class CouponsController:
    def __init__(self):
        self.model = CouponModel
        self.schema = CouponsResponseSchema

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
                'message': 'No se encontro el cupon en mención'
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
                'messsage': 'El cupon se creo con exito',
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
                    'messsage': 'El cupon se ha actualizado con exito',
                    'data': response.dump(record)
                }, 200
            return {
                'message': 'No se encontro el cupon en mención'
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
                    'message': 'Se deshabilito el cupon con exito'
                }, 200
            return {
                'message': 'No se encontro el cupon en mención'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500
