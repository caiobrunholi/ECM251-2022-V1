# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

import streamlit as st
from src.models.user import User
from src.controllers.user_controller import UserController
import time

# instancia de controller
controller=UserController()

# imagens
png_unknown = "assets./unknown_user.png"
png_female = "assets./female_user.png"
png_male = "assets./male_user.png"


# funcao de atualizacao da imagem / texto da tela de login / autorizacao de usuario
def update_profile_pic(png, user, password, but):
    if but == "Register":
        st.session_state["message"] = "Olá Novo Usuário"
    else:
        result = controller.pegar_user(username=user)
        print(result)
        if result != None and user == result.username and password == result.password:
            st.session_state["image"] = png
            st.session_state["message"] = f"Bem vindo {result.name}!"
            st.session_state["hello"]= result.name
            st.session_state["state"] = True
        else:
            st.session_state["image"] = png_unknown
            st.session_state["message"] = "Usuário e/ou Senha incorreto"
            st.session_state["state"] = False

# funcao para registrar novo usuario
def register_user(new_name, new_email, new_user, new_password, new_credit_card, new_account_credit):
    # usuario de teste
    # user = User(name='Fake', email='fake@email.com', username='Fake', password='fake', credit_card='creditfake', account_credit=1.0)
    user = User(name=new_name, email=new_email, username=new_user, password=new_password, credit_card=new_credit_card, account_credit=new_account_credit)
    success = controller.inserir_user(user)
    print(success)

    time.sleep(1)
    # permite o acesso a lojinha pos cadastro
    if success:
        st.session_state["state"] = True

def show_login_page():
    st.title("Login")

    with st.container():
        # funcoes de estado iniciais
        if "image" in st.session_state:
            st.image(st.session_state["image"],width=100)
        else:
            st.image(png_unknown,width=100)

        if "message" in st.session_state:
            st.write(st.session_state["message"])
        
        if "state" in st.session_state:
            st.session_state["state"]
        else:
            st.session_state["state"]=False
        
        if "register" in st.session_state:
            st.session_state["register"]
        else:
            st.session_state["register"]=False

        if "hello" in st.session_state:
            st.session_state["hello"]
        else:
            st.session_state["hello"]='Usuario(a)'

    # text input
        user = st.text_input('Usuario', 'Username')
        password = st.text_input('Senha', 'Password')

    # botoes
        login_but = st.button(
            label="Login", 
            help="Login do Usuário",
            on_click=update_profile_pic,
            kwargs={"png":"assets./female_user.png", "user":user, "password":password, "but":"Login"}
        )

        st.markdown("Não possui uma conta ainda?")
        register_but= st.button(
            label="Register", 
            help="Registro de usuário",
            on_click=update_profile_pic,
            kwargs={"png":"assets/unknown_user.png", "user":user, "password":password, "but":"Register"},
            disabled=st.session_state["state"]
        )

    if login_but:
        st.write("Login!")
        
    if register_but:
        st.write("Cadastrar usuário!")
        # text input
        new_name = st.text_input('Nome', 'NewName')
        new_email = st.text_input('Novo E-mail', 'E-mail')
        new_user = st.text_input('Novo Nome de Usuário', 'Username')
        new_password = st.text_input('Nova Senha', 'NewPassword')
        new_credit_card = st.text_input('Novo Cartão de Crédito', 'Credit Card') # Não implementado nessa versão
        new_account_credit = st.text_input('Novo Crédito de Conta', 0.0) # Não implementado nessa versão
        done_but = st.button(
            label="Done", 
            help="Finalizar Cadastro",
            on_click=register_user,
            kwargs={"new_name":new_name, "new_email":new_email, "new_user":new_user, "new_password":new_password, "new_credit_card":new_credit_card, "new_account_credit":new_account_credit}
        )
            

