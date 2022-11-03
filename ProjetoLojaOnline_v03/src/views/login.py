# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

import streamlit as st

# Login usando o user_controller ainda não implementado

# imagens
png_unknown = "assets./unknown_user.png"
png_female = "assets./female_user.png"
png_male = "assets./male_user.png"


# funcao de atualizacao da imagem e texto da tela de login
def update_profile_pic(png, user, password, but):
    if but == "Register":
        st.session_state["message"] = "Olá Novo Usuário"
    else:
        if user == "Fulana" and password == "1234":
            st.session_state["image"] = png
            st.session_state["message"] = "Bem vindo Fulana!"
            st.session_state["state"] = True
        else:
            st.session_state["image"] = png_unknown
            st.session_state["message"] = "Usuário e/ou Senha incorreto"
            st.session_state["state"] = False

def register_user():
    st.session_state["state"] = True
    
def show_login_page():
    st.title("Login")

    with st.container():
        # funcoes de estano iniciais
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
        # st.session_state["register"] = True
        # text input
        nwe_name = st.text_input('Nome', 'Name')
        new_email = st.text_input('Novo E-mail', 'E-mail')
        new_user = st.text_input('Novo Nome de Usuário', 'Username')
        new_password = st.text_input('Nova Senha', 'Password')
        new_credit_card = st.text_input('Novo Cartão de Crédito', 'Card') # Não implementado nessa versão
        new_account_credit = st.text_input('Novo Crédito de Conta', 'Credit') # Não implementado nessa versão
        done_but = st.button(
            label="Done", 
            help="Finalizar Cadastro",
            on_click=register_user,
            kwargs={}
             
        )
            

