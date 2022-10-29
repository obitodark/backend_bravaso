from email.policy import default
from app.models.base import BaseModel
from sqlalchemy import Column, Integer,String, ForeignKey,Boolean
from sqlalchemy.orm import relationship


class ImagesModel(BaseModel):
    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image = Column(String(255))
    status= Column(Boolean, default=True)

    imagesProduct=relationship('ImagesProductModel',uselist=True,back_populates='images')
    imagesUser=relationship('ImagesUserModel',uselist=True,back_populates='images')

  