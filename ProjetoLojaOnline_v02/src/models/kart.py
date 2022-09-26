# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from models.product import Product
class Kart():
    # construtor
    def __init__(self):
        self._products=[]
    
    # geters
    def get_total_value(self):
        total=0
        for product in self._products:
            total+=product.get_price()
        return total

    def get_quatity(self):
        return len(self._products)

    # adicionar ao carrinho
    def add_to_kart(self,product):
        self._products.append(product)

    # remover do carrinho
    def remove_from_kart(self, product):
        if product in self._products:
            self._products.remove(product)