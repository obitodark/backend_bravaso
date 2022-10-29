from app.models.base import BaseModel
from sqlalchemy import Column, Integer,Boolean, ForeignKey
from sqlalchemy.orm import relationship


class ImagesProductModel(BaseModel):
    __tablename__ = 'images_product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey('images.id'))
    product_id = Column(Integer, ForeignKey('products.id'))
    status=Column(Boolean,default=True)



    images=relationship('ImagesModel',uselist=False,back_populates='imagesProduct')
    product = relationship('ProductsModel', uselist=False, back_populates='images')

