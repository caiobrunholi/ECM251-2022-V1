# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3
class Product():
    # inicia classe
    def __init__(self, id, name, category, description, price, image) -> None:
        self.id = id
        self.name = name
        self.category = category
        self.description = description
        self.price = price
        self.image = image

    def __str__(self) -> str:
        return f'Product(id:{self.id}, name:{self.name}, category:{self.category}, description:{self.description}, price:{self.price}, image:{self.image})'

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
        return self._image

