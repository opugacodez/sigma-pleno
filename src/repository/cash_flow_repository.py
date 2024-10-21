from src.config.database import db
from src.model.cash_flow_model import CashFlow
from sqlalchemy.exc import SQLAlchemyError

class CashFlowRepository:
    @staticmethod
    def add_cash_flow(cash_flow_data):
        try:
            cash_flow = CashFlow(**cash_flow_data)
            db.session.add(cash_flow)
            db.session.commit()
            return cash_flow
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e

    @staticmethod
    def get_all_cash_flows():
        return CashFlow.query.all()

    @staticmethod
    def get_cash_flow_by_id(cash_flow_id):
        return CashFlow.query.get(cash_flow_id)
    
    @staticmethod
    def get_cash_flow_by_product_id(product_id):
        return CashFlow.query.filter_by(product_id=product_id).first()

    @staticmethod
    def update_cash_flow(cash_flow, updated_data):
        for key, value in updated_data.items():
            setattr(cash_flow, key, value)
        db.session.commit()

    @staticmethod
    def delete_cash_flow(cash_flow):
        db.session.delete(cash_flow)
        db.session.commit()
