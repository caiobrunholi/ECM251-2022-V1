from ttkbootstrap import LEFT
import ttkbootstrap as ttk

base=ttk.Window()

# Criando um botao
ttk.Button(
    base, #filho de quem
    text="Ola Mundo!",
    bootstyle="default",
).pack(side=LEFT, padx=10, pady=5) #onde fica dentro

# Ponto de entrada da interface
base.mainloop()