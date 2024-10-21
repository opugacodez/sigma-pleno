from src.repository.cash_flow_repository import CashFlowRepository
from src.schema.cash_flow_schema import cash_flow_schema, cash_flow_list_schema
from marshmallow import ValidationError

class CashFlowService:
    @staticmethod
    def create_cash_flow(cash_flow_data):
        try:
            validated_data = cash_flow_schema.load(cash_flow_data)
            return CashFlowRepository.add_cash_flow(validated_data)
        except ValidationError as err:
            raise ValueError(err.messages)

    @staticmethod
    def retrieve_cash_flows():
        cash_flows = CashFlowRepository.get_all_cash_flows()
        print(cash_flows)
        return cash_flow_list_schema.dump(cash_flows)

    @staticmethod
    def retrieve_cash_flow_by_id(cash_flow_id):
        cash_flow = CashFlowRepository.get_cash_flow_by_id(cash_flow_id)
        if not cash_flow:
            raise ValueError("Cash flow not found")
        return cash_flow_schema.dump(cash_flow)
    
    @staticmethod
    def retrieve_cash_flow_by_product_id(product_id):
        cash_flow = CashFlowRepository.get_cash_flow_by_product_id(product_id)
        if not cash_flow:
            raise ValueError("Cash flow not found")
        return cash_flow_schema.dump(cash_flow)

    @staticmethod
    def update_cash_flow(cash_flow_id, updated_data):
        cash_flow = CashFlowRepository.get_cash_flow_by_id(cash_flow_id)
        if not cash_flow:
            raise ValueError("Cash flow not found")
        
        try:
            validated_data = cash_flow_schema.load(updated_data)
            CashFlowRepository.update_cash_flow(cash_flow, validated_data)
            return cash_flow_schema.dump(cash_flow)
        except ValidationError as err:
            raise ValueError(err.messages)

    @staticmethod
    def delete_cash_flow(cash_flow_id):
        cash_flow = CashFlowRepository.get_cash_flow_by_id(cash_flow_id)
        if not cash_flow:
            raise ValueError("Cash flow not found")
        CashFlowRepository.delete_cash_flow(cash_flow)
