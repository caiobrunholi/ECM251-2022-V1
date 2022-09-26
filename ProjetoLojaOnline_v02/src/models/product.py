# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3
class Product():
    # inicia classe
    def __init__(self, name, category, description, price, image) -> None:
        self.name = name
        self.category = category
        self.desciption = description
        self.price = price
        self.image = image

    def __str__(self) -> str:
        return f'Product(name:{self.name}, category:{self.category}, description:{self.desciption}, price:{self.price})'

    # getters
    def get_name(self):
        return self._name
    
    def get_category(self):
        return self._category
    
    def get_description(self):
        return self._description

    def get_price(self):
        return self._price
    
    def get_image(self):
        return self.image

