from app.models.base import BaseModel
from sqlalchemy import Column, Integer, Boolean, Float, DateTime, String


class CouponModel(BaseModel):
    __tablename__ = 'coupons'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(50))
    percentage = Column(Float(precision=2))
    started_at = Column(DateTime)
    ended_at = Column(DateTime)
    status = Column(Boolean, default=True)
