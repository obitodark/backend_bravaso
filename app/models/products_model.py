
from xml.etree.ElementInclude import include
from app.models.base import BaseModel
from sqlalchemy import Column,Integer ,String,Float,ForeignKey,Boolean,Text
from sqlalchemy.orm import relationship

class ProductsModel(BaseModel):
    
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    description = Column(Text)
    price = Column(Float(precision=2))
    # image = Column(String(255))
    stock = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))  
    subcategory_id=Column(Integer,ForeignKey('subcategories.id')) 
    brand_id=Column(Integer, ForeignKey('brands.id')  )  
    source_id=Column(Integer, ForeignKey('source_product.id') )
    type_material_id=Column(Integer, ForeignKey('type_material.id'))
    status = Column(Boolean, default=True)
    weight = Column(Float(precision=2))
    # products = relationship('ProductModel', uselist=True, back_populates='category')
    category=relationship('CategoryModel',uselist=False,back_populates='product')
    subcategory=relationship('SubCategoryModel',uselist=False,back_populates='products')
    brand=relationship('BrandsModel',uselist=False,back_populates='products')
    shopping_carts = relationship('ShoppingCartModel', uselist=True, back_populates='product')
    favorite = relationship('FavoriteModel', uselist=True, back_populates='product')
    source_products=relationship('SourceProductModel',uselist=False,back_populates='product')
    shopping_carts = relationship('ShoppingCartModel', uselist=True, back_populates='product')
    images = relationship('ImagesProductModel', uselist=True, order_by="ImagesProductModel.id" ,lazy='dynamic',back_populates='product')
    type_materials=relationship('TypeMaterialModel',uselist=True, )

#   ordenar -> https://docs.sqlalchemy.org/en/14/orm/extensions/orderinglist.html
