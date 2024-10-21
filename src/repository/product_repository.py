from src.model.product_model import Product, db
from src.schema.product_schema import product_schema, product_list_schema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError


class ProductRepository:

    @staticmethod
    def get_all_products():
        try:
            products = Product.query.all()
            return product_list_schema.dump(products), 200
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500

    @staticmethod
    def get_product_by_id(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return {"error": "Product not found"}, 404
            return product_schema.dump(product), 200
        except SQLAlchemyError as e:
            return {"error": str(e)}, 500

    @staticmethod
    def add_product(product_data):
        try:
            validated_data = product_schema.load(product_data)
        except ValidationError as err:
            return {"errors": err.messages}, 400

        new_product = Product(
            name=validated_data.name,
            description=validated_data.description,
            amount=validated_data.amount
        )

        try:
            db.session.add(new_product)
            db.session.commit()
            return product_schema.dump(new_product), 201
        except SQLAlchemyError as e:
            print(str(e))
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def update_product(product_id, product_data):
        try:
            product = Product.query.get(product_id)
            if not product:
                return {"error": "Product not found"}, 404

            try:
                validated_data = product_schema.load(product_data)
            except ValidationError as err:
                return {"errors": err.messages}, 400
    
            product.name = validated_data.name
            product.description = validated_data.description
            product.amount = validated_data.amount

            db.session.add(product)
            db.session.commit()
            return product_schema.dump(product), 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 500

    @staticmethod
    def delete_product(product_id):
        try:
            product = Product.query.get(product_id)
            if not product:
                return {"error": "Product not found"}, 404

            db.session.delete(product)
            db.session.commit()
            return {"message": "Product deleted successfully"}, 200
        except SQLAlchemyError as e:
            db.session.rollback()
            return {"error": str(e)}, 500