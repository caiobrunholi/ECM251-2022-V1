# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3
from src.models.user import User
from src.dao.user_dao import UserDAO

# Dados de Usuário:
# name, email, username, password, credit_card, account_credit

class UserController():
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