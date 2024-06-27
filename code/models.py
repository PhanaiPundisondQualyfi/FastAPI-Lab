from database import Base
from sqlalchemy import Column, Integer, String, Float

class Items(Base):
    __tablename__ = 'ItemsTable'

    id = Column(Integer, primary_key=True, index=True, autoincrement='auto')
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    tax = Column(Float)
