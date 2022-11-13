# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3
import sqlite3
from src.models.user import User

class UserDAO:
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    # cria instancia
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    # conecta ao banco de dados
    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db', check_same_thread=False)
        print('connected to db')
        
    # funcoes
    def pegar_user(self, username):
        print('pegar user DAO function')
        self.cursor = self.conn.cursor()

        print(f"""
            string to be excuted
            SELECT * FROM User
            WHERE username = '{username}';
        """)
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE username = '{username}';
        """)
        user = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            user = User(name=resultado[0], email=resultado[1], username=resultado[2], password=resultado[3], credit_card=resultado[4], account_credit=resultado[5])
        self.cursor.close()
        return user

    def inserir_user(self, user):
        try:
            print('insert user DAO function')
            print(user)
            print(user.credit_card)
            print(f"""
                string to be executed
                INSERT INTO User (name, email, username, password, creditcard, accountcredit)
                VALUES('{user.name}', '{user.email}', '{user.username}', '{user.password}', '{user.credit_card}', {user.account_credit});
            """)

            self.cursor = self.conn.cursor()
            
            self.cursor.execute(f"""
                INSERT INTO User (name, email, username, password, creditcard, accountcredit)
                VALUES('{user.name}', '{user.email}', '{user.username}', '{user.password}', '{user.credit_card}', {user.account_credit});
            """)
            self.conn.commit()
            print('commited')
            self.cursor.close()
            print('closed')
        except:
            return False
        return True
    

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM User;
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name=resultado[0], email=resultado[1], username=resultado[2], password=resultado[3], credit_card=resultado[4], account_credit=resultado[5]))
        self.cursor.close()
        return resultados

    def atualizar_user(self, user):
        print('update user DAO function')
        try:
            self.cursor = self.conn.cursor()
            print(f"""
                string to be executed
                UPDATE User SET
                email = '{user.email}',
                password = '{user.password}'
                WHERE username = '{user.username}'
            """)
            self.cursor.execute(f"""
                UPDATE User SET
                email = '{user.email}',
                password = '{user.password}'
                WHERE username = '{user.username}'
            """)
            self.conn.commit()
            print('commited')
            self.cursor.close()
            print('closed')
        except:
            return False
        return True

    def deletar_user(self, username):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM User 
                WHERE username = '{username}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def search_all_for_name(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE name LIKE '{name}%';
        """)
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(User(name=resultado[0], email=resultado[1], username=resultado[2], password=resultado[3], credit_card=resultado[4], account_credit=resultado[5]))
        self.cursor.close()
        return resultados