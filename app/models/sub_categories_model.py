from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean,ForeignKey
from sqlalchemy.orm import relationship



class SubCategoryModel(BaseModel):
    __tablename__ = 'subcategories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    id_category=Column(Integer,ForeignKey('categories.id'))

    products=relationship('ProductsModel',uselist=True,back_populates='subcategory')
    # category =relationship('CategoryModel',uselist=True,back_populates='subcategory')
    
    # products = relationship('ProductModel', uselist=True, back_populates='category')
