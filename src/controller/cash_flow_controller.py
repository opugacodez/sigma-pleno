from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from src.service.cash_flow_service import CashFlowService
from src.schema.cash_flow_schema import cash_flow_schema
from marshmallow import ValidationError

cash_flow_bp = Blueprint('cash_flow', __name__)

@cash_flow_bp.route('/api/cash-flow', methods=['POST'])
@jwt_required
def add_cash_flow():
    cash_flow_data = request.json
    try:
        cash_flow = CashFlowService.create_cash_flow(cash_flow_data)
        return cash_flow_schema.dump(cash_flow), 201
    except ValueError as e:
        return {"errors": str(e)}, 400
    except Exception as e:
        return {"error": str(e)}, 500

@cash_flow_bp.route('/api/cash-flow', methods=['GET'])
@jwt_required
def get_cash_flows():
    cash_flows = CashFlowService.retrieve_cash_flows()
    return cash_flows, 200

@cash_flow_bp.route('/api/cash-flow/<int:id>', methods=['GET'])
@jwt_required
def get_cash_flow(id):
    try:
        cash_flow = CashFlowService.retrieve_cash_flow_by_id(id)
        return cash_flow, 200
    except ValueError as e:
        return {"error": str(e)}, 404

@cash_flow_bp.route('/api/cash-flow/<int:id>', methods=['PUT'])
@jwt_required
def update_cash_flow(id):
    cash_flow_data = request.json
    try:
        cash_flow = CashFlowService.update_cash_flow(id, cash_flow_data)
        return cash_flow, 200
    except ValueError as e:
        return {"error": str(e)}, 404
    except Exception as e:
        return {"error": str(e)}, 500

@cash_flow_bp.route('/api/cash-flow/<int:id>', methods=['DELETE'])
@jwt_required
def delete_cash_flow(id):
    try:
        CashFlowService.delete_cash_flow(id)
        return {"message": "Cash flow deleted"}, 204
    except ValueError as e:
        return {"error": str(e)}, 404
    except Exception as e:
        return {"error": str(e)}, 500
