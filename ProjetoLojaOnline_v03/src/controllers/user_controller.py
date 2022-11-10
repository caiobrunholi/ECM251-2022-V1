# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3
from src.models.user import User
from src.dao.user_dao import UserDAO

# Login usando o user_controller ainda não implementado

# Dados de Usuário:
# name, email, username, password, credit_card, account_credit

# c1 = CreditCard
class UserController():
    # def __init__(self) -> None:
    #     #Carrega os dados dos usuários
    #     self.users = [
    #         User(name="joao", username="joao", password="arroz", email="joao@mail.com", credit_card=c1, account_credit=100),
    #         User(name="joao2", username="joao2", password="arroz2", email="joao@amaarroz.com", credit_card=c1, account_credit=100),
    #         User(name="tais", username="tais", password="petacular", email="tais_@condida.com", credit_card=c1, account_credit=100),
    #         User(name="Fulana", username="Fulana", password="1234", credit_card=c1, account_credit=100)
    #     ]

    # def checkUser(self,user):
    #     return user in self.users

    # def checkLogin(self, username, password):
    #     user_teste = User(username=username, password=password, email=None)
    #     for user in self.users:
    #         if user.username == user_teste.username and user.password == user_teste.password:
    #             return True
    #     return False

    def __init__(self) -> None:
        pass
    
    def pegar_user(self, username) -> User:
        user = UserDAO.get_instance().pegar_user(username)
        return user

    def inserir_user(self, user) -> bool:
        try:
            UserDAO.get_instance().inserir_user(user)
        except:
            return False
        return True

    def pegar_todos_user(self) -> list[User]:
        users = UserDAO.get_instance().get_all()
        return users
    
    def atualizar_user(self, user) -> bool:
        return UserDAO.get_instance().atualizar_user(user)

    def deletar_user(self, username) -> bool:
        return UserDAO.get_instance().deletar_user(username)

    def buscar_todos_user_nome(self, name) -> list[User]:
        users = UserDAO.get_instance().search_all_for_name(name)
        return users