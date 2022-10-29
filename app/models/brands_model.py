from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship



class BrandsModel(BaseModel):
    __tablename__ = 'brands'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    
    products = relationship('ProductsModel', uselist=True, back_populates='brand')
