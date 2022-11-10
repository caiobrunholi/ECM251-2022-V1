import sqlite3
from src.models.user import User

class UserDAO:
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./databases/sqlite.db')

    def pegar_user(self, username):
        self.cursor = self.conn.cursor()
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
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO User (name, email, username. password, creditcard, accountcredit)
                VALUES(?,?,?,?,?,?);
            """, (user.name, user.email, user.username, user.password, user.creditcard, user.accountcredit))
            self.conn.commit()
            self.cursor.close()

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
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE User SET
                name = '{user.name}',
                email = '{user.email}',
                password = '{user.password}',
                creditcard = '{user.creditcard}',
                accountcredit = {user.accountcredit},
                WHERE username = '{user.username}'
            """)
            self.conn.commit()
            self.cursor.close()
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