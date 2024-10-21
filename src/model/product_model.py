from src.config.database import db
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
    amount = Column(Float, nullable=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)
    deleted_at = Column(DateTime(timezone=True), nullable=True)

    def __init__(self, name, description, amount):
        self.name = name
        self.description = description
        self.amount = amount
