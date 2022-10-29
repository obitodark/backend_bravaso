from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship



class SourceProductModel(BaseModel):
    __tablename__ = 'source_product'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    
    # products = relationship('ProductModel', uselist=True, back_populates='category')
    # subcategory=relationship('SubCategoryModel',uselist=True,back_populates='category')
    product=relationship('ProductsModel',uselist=True,back_populates='source_products')