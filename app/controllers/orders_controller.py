from app import db
from app.models.orders_model import OrderModel
from app.models.orders_items_model import OrderItemModel
from app.controllers.shopping_carts_controller import ShoppingCartsController
from flask_jwt_extended import current_user
from shortuuid import ShortUUID
from app.utils.mercadopago import Mercadopago


class OrderController:
    def __init__(self):
        self.model = OrderModel
        self.model_item = OrderItemModel
        self.shopping_cart = ShoppingCartsController()
        self.user_id = current_user['id']

        self.mercadopago = Mercadopago()

    def create(self):
        try:
            shopping_cart = self.shopping_cart._getAllItems()
            products = shopping_cart['data']

            if not products:
                raise Exception('El carrito de compras esta vacio')

            prices = shopping_cart['prices']
            correlative = ShortUUID().random(length=5)

            order = self.model.create(
                user_id=self.user_id,
                total_price=prices['total'],
                subtotal_price=prices['subtotal'],
                igv_price=prices['igv'],
                discount_price=0.00,
                correlative=correlative
            )

            order_items = [
                self.model_item.create(
                    order_id=order.id,
                    product_id=item['product']['id'],
                    price=item['product']['price'],
                    quantity=item['quantity']
                )
                for item in products
            ]

            checkout = self.__createCheckout(order, products)
            init_point = checkout['init_point']

            order.checkout_id = checkout['id']
            order.checkout_url = init_point

            # Guardar el pedido y los productos del pedido
            db.session.add(order)
            db.session.add_all(order_items)

            # Limpiar el carrito de compras
            self.shopping_cart._deleteAllItems()

            # Restar el stock de los productos
            # Para ustedes :)

            # Mandamos los cambios a la BD
            db.session.commit()

            # Retornar el objeto de la orden
            return {
                'message': 'Se creo la orden con exito',
                'data': {
                    'checkout_url': init_point
                }
            }, 200
        except Exception as e:
            return {
                'message': 'Ocurrio un error',
                'error': str(e)
            }, 500

    def __createCheckout(self, order, products):
        payer = {
            'name': current_user['name'],
            'surname': current_user['last_name'],
            'email': current_user['email']
        }

        items = [
            {
                'id': item['product']['id'],
                'title': item['product']['name'],
                'quantity': item['quantity'],
                'unit_price': round(
                    item['product']['price'] + (item['product']['price'] * self.shopping_cart.igv), 2),
                'currency_id': 'PEN',
                'picture_url': item['product']['images'][0]['images']['image']
            }
            for item in products
        ]

        return self.mercadopago.createPreferences(payer, items, order.correlative)
 