# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from src.models.product import Product

# Dados de Produto:
# name, category, description, price, image
class ProductController():
    def __init__(self) -> None:
        #Carrega os produtos

        # pc_gamer=Product("PC Gamer", "Eletronicos", "Um PC Monstro com os specs mais cabulosos do planeta terra", 1000, "assets./pcgamer.png")
        
        self.products = [
            Product("PC Gamer", "Eletronicos", "Um PC Monstro com os specs mais cabulosos do planeta terra", 1000, "assets./pcgamer.png"),
            Product("Teclado Gamer", "Eletronicos", "Teclado colorido que faz tec tec tec", 100, "assets./keyboard.png"),
            Product("Mouse Gamer", "Eletronicos", "Mouse colorido incareditavelmente rápido", 100, "assets./mouse.png"),
            Product("Smartphone", "Eletronicos", "Também faz ligações, mas quem liga hoje em dia?", 1000, "assets./smartphone.png"),
            Product("MineConstructor", "Jogos", "Por motivos de Copyright esse jogo não é uma cópia de Minecraft", 20, "assets./minecraft.png"),
            Product("CS GO", "Jogos", "CSzinho da massa", 10, "assets./csgo.png"),
            Product("Monopoly", "Jogos", "Quem disse que só precisava ser jogos de computador?", 25, "assets./monopoly.png"),
            Product("X-TUDÃO", "Comida", "Um X-Tudo mais completo que o completão", 20, "assets./burguer.png"),
            Product("Salgadinho", "Comida", "Nós dois sabemos que você vai continuar com fome depois", 5, "assets./chips.png"),
            Product("Redbull", "Comida", "Um energético que só está aqui pois patrocina o CA", 6, "assets./redbull.png"),
            Product("Suco de Açaí com Paçoquinha", "Comida", "Esse suco vai te dar um boost de energia incareditaaaAAAAAVVVEEEELLLLLL! (Não recomendado para pessoas de intestino fraco)", 12, "assets./acai.jpg")
        ]
