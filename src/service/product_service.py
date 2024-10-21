from src.repository.product_repository import ProductRepository


class ProductService:

    @staticmethod
    def list_products():
        """Retorna todos os produtos com tratamento de erro adequado."""
        products, status_code = ProductRepository.get_all_products()
        return products, status_code

    @staticmethod
    def get_product(product_id):
        """Retorna um produto por ID com tratamento de erro."""
        product, status_code = ProductRepository.get_product_by_id(product_id)
        return product, status_code

    @staticmethod
    def add_product(product_data):
        """
        Adiciona um novo produto com base nos dados fornecidos.
        :param product_data: Um dicionário contendo os dados do produto.
        """
        product, status_code = ProductRepository.add_product(product_data)
        return product, status_code

    @staticmethod
    def modify_product(product_id, product_data):
        """
        Atualiza um produto existente com base no ID e nos novos dados fornecidos.
        :param product_id: O ID do produto a ser atualizado.
        :param product_data: Um dicionário contendo os novos dados do produto.
        """
        product, status_code = ProductRepository.update_product(product_id, product_data)
        return product, status_code

    @staticmethod
    def remove_product(product_id):
        """
        Remove um produto com base no ID.
        :param product_id: O ID do produto a ser removido.
        """
        response, status_code = ProductRepository.delete_product(product_id)
        return response, status_code
