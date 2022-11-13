# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from src.models.product import Product
from src.dao.product_dao import ProductDAO

# Dados de Produto:
# id, name, category, description, price, image
class ProductController():
    def __init__(self) -> None:
        pass

    def pegar_produto(self, id) -> Product:
            produto = ProductDAO.get_instance().pegar_produto(id)
            return produto

    def inserir_produto(self, produto) -> bool:
        try:
            ProductDAO.get_instance().inserir_produto(produto)
        except:
            return False
        return True

    def pegar_todos_produtos(self) -> list[Product]:
        products = ProductDAO.get_instance().get_all()
        return products
    
    def atualizar_produto(self, product) -> bool:
        return ProductDAO.get_instance().atualizar_produto(product)

    def deletar_produto(self, id) -> bool:
        return ProductDAO.get_instance().deletar_item(id)

    def buscar_todos_produtos_name(self, name) -> list[Product]:
        products = ProductDAO.get_instance().search_all_for_name(name)
        return products

