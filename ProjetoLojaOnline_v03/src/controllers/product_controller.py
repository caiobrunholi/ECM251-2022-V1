# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from src.models.product import Product
from src.dao.product_dao import ProductDAO

# Dados de Produto:
# id, name, category, description, price, image
class ProductController():
    def __init__(self) -> None:
        #Carrega os produtos

        # pc_gamer=Product(10001,"PC Gamer", "Eletronicos", "Um PC Monstro com os specs mais cabulosos do planeta terra", 1000, "assets./pcgamer.png")
        # PRECISO INICIAR ASSIM??????
        
        # self.products = [
        #     Product(10001,"PC Gamer", "Eletronicos", "Um PC Monstro com os specs mais cabulosos do planeta terra", 1000, "assets./pcgamer.png"),
        #     Product("10002, Teclado Gamer", "Eletronicos", "Teclado colorido que faz tec tec tec", 100, "assets./keyboard.png"),
        #     Product(10003, "Mouse Gamer", "Eletronicos", "Mouse colorido incareditavelmente rápido", 100, "assets./mouse.png"),
        #     Product(10004, "Smartphone", "Eletronicos", "Também faz ligações, mas quem liga hoje em dia?", 1000, "assets./smartphone.png"),
        #     Product(20001, "MineConstructor", "Jogos", "Por motivos de Copyright esse jogo não é uma cópia de Minecraft", 20, "assets./minecraft.png"),
        #     Product(20002, "CS GO", "Jogos", "CSzinho da massa", 10, "assets./csgo.png"),
        #     Product(20003, "Monopoly", "Jogos", "Quem disse que só precisava ser jogos de computador?", 25, "assets./monopoly.png"),
        #     Product(30001, "X-TUDÃO", "Comida", "Um X-Tudo mais completo que o completão", 20, "assets./burguer.png"),
        #     Product(30002, "Salgadinho", "Comida", "Nós dois sabemos que você vai continuar com fome depois", 5, "assets./chips.png"),
        #     Product(30003, "Redbull", "Comida", "Um energético que só está aqui pois patrocina o CA", 6, "assets./redbull.png"),
        #     Product(30004, "Suco de Açaí com Paçoquinha", "Comida", "Esse suco vai te dar um boost de energia incareditaaaAAAAAVVVEEEELLLLLL! (Não recomendado para pessoas de intestino fraco)", 12, "assets./acai.jpg")
        # ]

        pass

    def pegar_produto(self, id) -> Product:
            produto = ProductDAO.get_instance().pegar_produto(id)
            return produto

    def inserir_produto(self, item) -> bool:
        try:
            ProductDAO.get_instance().inserir_item(item)
        except:
            return False
        return True

    def pegar_todos_produtos(self) -> list[Product]:
        products = ProductDAO.get_instance().get_all()
        return products
    
    def atualizar_produto(self, product) -> bool:
        return ProductDAO.get_instance().atualizar_item(product)

    def deletar_produto(self, id) -> bool:
        return ProductDAO.get_instance().deletar_item(id)

    def buscar_todos_produtos_name(self, name) -> list[Product]:
        products = ProductDAO.get_instance().search_all_for_name(name)
        return products

