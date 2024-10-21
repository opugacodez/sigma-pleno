from flask import Blueprint, jsonify, request
from src.service.user_service import UserService


user_blueprint = Blueprint('auth', __name__)

@user_blueprint.route('/auth/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Username, email, and password are required."}), 400

    result = UserService.register_user(username, email, password)
    return jsonify(result[0]), result[1]

@user_blueprint.route('/auth/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    result = UserService.login_user(username, password)
    return jsonify(result[0]), result[1]
