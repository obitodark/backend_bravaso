from app.models.base import BaseModel
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class FavoriteModel(BaseModel):
    __tablename__ = 'favorites'

    id = Column(Integer, primary_key=True ,autoincrement=True)
    product_id= Column(Integer,ForeignKey('products.id'))
    user_id=Column(Integer, ForeignKey('users.id'))
    product = relationship('ProductsModel', uselist=False, back_populates='favorite')