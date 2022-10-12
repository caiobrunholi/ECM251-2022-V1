# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

# RESPONSÁVEL PELO CONTROLE DE PAGINAS EXIBIDAS

# Imports de bibliotecas e classes
from src.views.login import show_login_page
from src.views.home import show_home_page
import streamlit as st

# Controle ddas paginas mostradas
if "state" in st.session_state:
    st.session_state["state"]
else:
    st.session_state["state"]=False
class Main():
    def __init__(self) -> None:
        if st.session_state["state"]: #Verificação de estado de login
            show_home_page()
        else:
            show_login_page()

app = Main()