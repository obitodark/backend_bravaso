from app.models.base import BaseModel
from sqlalchemy import Column, Integer,Boolean, ForeignKey
from sqlalchemy.orm import relationship


class ImagesUserModel(BaseModel):
    __tablename__ = 'images_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey('images.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    status=Column(Boolean,default=True)



    images=relationship('ImagesModel',uselist=False,back_populates='imagesUser')
    user = relationship('UserModel', uselist=False, back_populates='imagesUser')