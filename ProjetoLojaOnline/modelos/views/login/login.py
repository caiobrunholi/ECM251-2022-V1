from asyncio.windows_events import NULL
from cgitb import text
from turtle import color
from unittest.mock import DEFAULT
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import PhotoImage

class LoginUI():
    def _construir_base(self):
        janela = ttk.Window(
            title="Projeto Loja Online",
            size= (1024,400),
            position= (100,100),
            minsize= (600,300),
            maxsize= (1800,900),
            alpha=1.0
        )
        janela.iconphoto(False, PhotoImage(file='shopping_bag.png'))
        return janela

    def _criar_botao(self, texto, acao):
        botao = ttk.Button(
            self.base,
            text=texto,
            bootstyle=(DEFAULT),
            command=acao,
        )
        #botao.style 0xDA28D4
        return botao

    def _criar_texto(self, guardar):
        return ttk.Entry(
            self.base,
            textvariable=guardar,
        )

    def _criar_frame(self):
        return ttk.Frame(
            bootstyle="dark"
        )

    def __init__(self) -> None:
        self.base = self._construir_base()
        self.login_bot = self._criar_botao(texto="Log In", acao=self.login_user)
        self.login_bot.grid(row=5, column=1,ipadx=10)
        self.valor_digitado = ""
        self.user_text = self._criar_texto(guardar=self.valor_digitado)
        self.user_text.grid(row=2, column=1, padx=5, pady=5, ipadx=100)
        self.pswd_text = self._criar_texto(guardar=self.valor_digitado)
        self.pswd_text.grid(row=3, column=1, padx=5, pady=5, ipadx=100)
        self.frame = self._criar_frame()
        self.frame.grid(row=2, column=5, padx=5, pady=5)

    def login_user(self):
        print('User:',self.user_text.get())
        print('Password:',self.pswd_text.get())
        print('User Logged In!')
        
    def run(self):
        self.base.mainloop()


if __name__ == "__main__":
    app = LoginUI()
    app.run()