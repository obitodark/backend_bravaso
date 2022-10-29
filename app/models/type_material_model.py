from app.models.base import BaseModel
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship



class TypeMaterialModel(BaseModel):
    __tablename__ = 'type_material'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    status = Column(Boolean, default=True)
    
    # product=relationship('ProductsModel',uselist=True,back_populates='type_materials')
   