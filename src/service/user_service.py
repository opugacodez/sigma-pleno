from src.repository.user_repository import UserRepository
from src.model.user_model import User
from flask_jwt_extended import create_access_token


class UserService:
    @staticmethod
    def register_user(username, email, password):
        existing_user = UserRepository.get_user_by_username(username)
        if isinstance(existing_user, tuple) and existing_user[1] == 404:
            new_user_data = {
                "username": username,
                "email": email,
                "password": password
            }
            return UserRepository.add_user(new_user_data)
        return {"error": "User already exists."}, 409

    @staticmethod
    def login_user(username, password):
        user_data = UserRepository.get_user_by_username(username)
        if isinstance(user_data, tuple) and user_data[1] == 200:
            user = User.query.filter_by(username=username).first()
            if user and user.check_password(password):
                access_token = create_access_token(identity={"username": user.username})
                return {"access_token": access_token}, 200
            return {"error": "Invalid credentials."}, 401
        return user_data
