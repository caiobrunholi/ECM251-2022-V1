import sqlite3
from src.models.product import Product
class ProductDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Products;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], category=resultado[2], description=resultado[3], image=resultado[4], price=resultado[5]))
        self.cursor.close()
        return resultados
    
    def inserir_produto(self, product):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Product(id,name,category,description,price,image)
            VALUES(?,?,?,?,?,?);
        """, (product.id, product.name, product.category, product.description, product.price, product.image))
        self.conn.commit()
        self.cursor.close()
    def pegar_produto(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE id = '{id}';
        """)
        product = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            product = Product(id=resultado[0], name=resultado[1], category=resultado[2], description=resultado[3], image=resultado[4], price=resultado[5])
        self.cursor.close()
        return product
    
    def atualizar_produto(self, product):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Product SET
                name = '{product.name}',
                category = '{product.category}',
                description = '{product.description}',
                price = {product.price},
                image = '{product.image}',
                WHERE id = {product.id}
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def deletar_produto(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Products 
                WHERE id = {id}
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def search_all_for_name(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE nome LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], category=resultado[2], description=resultado[3], image=resultado[4], price=resultado[5]))
        self.cursor.close()
        return resultados
