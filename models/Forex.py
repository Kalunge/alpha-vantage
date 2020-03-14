from sqlalchemy import Column, String, Integer, Float, DateTime
from app import db
import datetime



class Forexx(db.Model):
    __tablename__ = 'forex'
    id = Column(Integer, primary_key=True)
    From = Column(String)
    To = Column(String)
    Open = Column(Float)
    High = Column(Float)
    Low = Column(Float)
    Close = Column(Float)
    Datetime = Column(DateTime, default=datetime.datetime.now)


