from app.models.base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.orderinglist import ordering_list

class ShoppingCartModel(BaseModel):
    __tablename__ = 'shopping_cart'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    quantity = Column(Integer)
    
    product = relationship('ProductsModel', uselist=False,order_by="ProductsModel.id",collection_class=ordering_list('id'),back_populates='shopping_carts')
