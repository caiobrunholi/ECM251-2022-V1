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

