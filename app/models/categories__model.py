from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship



class CategoryModel(BaseModel):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    
    # products = relationship('ProductModel', uselist=True, back_populates='category')
    # subcategory=relationship('SubCategoryModel',uselist=False,back_populates='category')
    product=relationship('ProductsModel',uselist=True,back_populates='category')