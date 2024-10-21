from marshmallow import Schema, fields, post_load
from src.model.cash_flow_model import CashFlow

class CashFlowSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    total_value = fields.Float(required=True)

    @post_load
    def make_cash_flow(self, data, **kwargs):
        return CashFlow(**data)

cash_flow_schema = CashFlowSchema()
cash_flow_list_schema = CashFlowSchema(many=True)