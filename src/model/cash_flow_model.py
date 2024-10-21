from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.config.database import db

class CashFlow(db.Model):
    __tablename__ = 'cash_flow'

    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    total_value = Column(Float, nullable=False)

    product = relationship('Product', back_populates='cash_flows')

    def __init__(self, product_id, quantity, total_value):
        self.product_id = product_id
        self.quantity = quantity
        self.total_value = total_value
