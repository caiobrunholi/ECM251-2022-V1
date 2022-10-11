# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from src.models.credit_card import CreditCard
class User():
    def __init__(self, name, email, username, password, credit_card, account_credit):
        self.name = name
        self.email = email
        self.username = username
        self.password = password
        self.credit_card = credit_card
        self.account_credit = account_credit

    def __str__(self) -> str:
        return f'User(name:{self.name}, email:{self.email}, username:{self.username}, password:{self.password}, account credit:{self.account_credit})'