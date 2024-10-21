from src.config.database import db
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime
)
from sqlalchemy.sql import func


class Product(db.Model):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    description = Column(String(255))
    price = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    cash_flows = relationship('CashFlow', back_populates='product')

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
