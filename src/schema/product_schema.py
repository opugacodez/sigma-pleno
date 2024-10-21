from marshmallow import Schema, fields, post_load, ValidationError
from src.model.product_model import Product


def validate_amount(value):
    if value < 0:
        raise ValidationError("Amount must be a positive number.")


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=lambda x: len(x) <= 30)
    description = fields.Str(validate=lambda x: len(x) <= 255)
    amount = fields.Float(required=True, validate=validate_amount)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    deleted_at = fields.DateTime(allow_none=True)

    @post_load
    def make_product(self, data, **kwargs):
        return Product(**data)


product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)
