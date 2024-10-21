from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from src.service.product_service import ProductService
from src.schema.product_schema import product_schema, product_list_schema
from marshmallow import ValidationError

main = Blueprint('products', __name__)

@main.route('/api/products', methods=['GET'])
@jwt_required()
def get_products():
    """Retorna todos os produtos."""
    products, status_code = ProductService.list_products()
    if status_code == 200:
        return jsonify(products), 200
    return jsonify({'error': 'Erro ao listar produtos'}), status_code


@main.route('/api/products/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product(product_id):
    """Retorna um produto pelo ID."""
    product, status_code = ProductService.get_product(product_id)
    if status_code == 200:
        return jsonify(product), 200
    return jsonify({'error': f'Produto com ID {product_id} não encontrado'}), status_code


@main.route('/api/products', methods=['POST'])
@jwt_required()
def add_product():
    """Adiciona um novo produto."""
    try:
        product_data = request.json
        product, status_code = ProductService.add_product(product_data)
        if status_code == 201:
            return jsonify(product), 201
        return jsonify({'error': 'Erro ao adicionar o produto'}), status_code
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/api/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update_product(product_id):
    """Atualiza um produto existente."""
    try:
        product_data = request.json
        product, status_code = ProductService.modify_product(product_id, product_data)
        if status_code == 200:
            return jsonify(product), 200
        return jsonify({'error': 'Erro ao atualizar produto'}), status_code
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@main.route('/api/products/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product(product_id):
    """Remove um produto."""
    response, status_code = ProductService.remove_product(product_id)
    if status_code == 200:
        return jsonify({'message': f'Produto com ID {product_id} removido com sucesso'}), 200
    return jsonify({'error': f'Produto com ID {product_id} não encontrado'}), status_code
