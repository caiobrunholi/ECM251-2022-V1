import ttkbootstrap as ttk
from tkinter import PhotoImage
from ttkbootstrap import LEFT

base = ttk.Window(
    title="Minha GUI Mauá",
    size=(1024,400),
    position=(100,100),
    minsize=(600,300),
    maxsize=(1800,900),
    alpha=1.0
)

base.iconphoto(False, PhotoImage(file='calculator.png'))

def acao_botao():
    print("Click!")

# Criando um botao
ttk.Button(
    base, #filho de quem
    text="Ola Mundo!",
    bootstyle="default",
    command=acao_botao
).pack(side=LEFT, padx=10, pady=5) #onde fica dentro

base.mainloop()