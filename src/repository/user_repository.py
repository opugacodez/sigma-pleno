from src.model.user_model import User, db
from src.schema.user_schema import user_schema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError
from werkzeug.security import generate_password_hash


class UserRepository:

    @staticmethod
    def get_user_by_username(username):
        try:
            user = User.query.filter_by(username=username).first()
            if not user:
                return {"error": "User not found"}, 404
            return user_schema.dump(user), 200
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500

    @staticmethod
    def add_user(user_data):
        try:
            validated_data = user_schema.load(user_data)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        new_user = User(
            username=validated_data.username,
            email=validated_data.email,
            password=generate_password_hash(validated_data.password, 'pbkdf2:sha256')
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            return user_schema.dump(new_user), 201
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def update_user(user_id, user_data):
        try:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404

            try:
                validated_data = user_schema.load(user_data)
            except ValidationError as err:
                return {"errors": err.messages}, 400

            user.username = validated_data.username
            user.email = validated_data.email
            user.password = generate_password_hash(validated_data.password, 'pbkdf2:sha256')

            db.session.commit()
            return user_schema.dump(user), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
            if not user:
                return {"error": "User not found"}, 404

            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted successfully"}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 500