from app import db
from app.models.shopping_cart_model import ShoppingCartModel
from app.schemas.shopping_carts_schema import ShoppingCartsResponseSchema
from flask_jwt_extended import current_user


class ShoppingCartsController:
    def __init__(self):
        self.model = ShoppingCartModel
        self.schema = ShoppingCartsResponseSchema
        self.user_id = current_user['id']
        self.igv = 0.18
        self.prices = {
            'total': 0,
            'subtotal': 0,
            'igv': 0
        }

    def all(self):
        try:
            return self._getAllItems(), 200
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def update(self, data):
        try:
            action = 'creo'

            if record := self.model.where(
                user_id=self.user_id,
                product_id=data['product_id']
            ).first():
                action = 'actualiza'
                record.update(**data)
            else:
                data['user_id'] = self.user_id
                record = self.model.create(**data)

            db.session.add(record)
            db.session.commit()

            return {
                'message': f'Se {action} el producto en el carrito'
            }, 200
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def delete(self, product_id):
        try:
            if record := self.model.where(
                user_id=self.user_id,
                product_id=product_id
            ).first():
                record.delete()
                db.session.commit()
                return {
                    'message': 'Se elimino el producto con exito'
                }, 200
            return {
                'message': 'No se encontro el producto en mencion'
            }, 404
        except Exception as e:
            db.session.rollback()
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def _getAllItems(self):
        records = self.model.where(user_id=self.user_id).all()
        response = self.schema(many=True)
        data = response.dump(records)

        if records:
            for item in data:
                price = item['product']['price']
                quantity = item['quantity']
                self.prices['subtotal'] += price * quantity

            self.prices['igv'] = round(
                self.prices['subtotal'] * self.igv, 2)
            self.prices['total'] = round(
                self.prices['subtotal'] + self.prices['igv'], 2)

        return {
            'data': data,
            'prices': self.prices
        }

    def _deleteAllItems(self):
        records = self.model.where(user_id=self.user_id).all()
        for record in records:
            record.delete()

        db.session.commit()
