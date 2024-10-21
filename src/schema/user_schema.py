from marshmallow import Schema, fields, post_load
from src.model.user_model import User


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=lambda x: len(x) <= 30)
    email = fields.Str(required=True, validate=lambda x: len(x) <= 50)
    password = fields.Str(required=True, load_only=True)

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)


user_schema = UserSchema()
