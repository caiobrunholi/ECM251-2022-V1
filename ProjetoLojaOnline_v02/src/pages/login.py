import streamlit as st

png_unknown = "assets./unknown_user.png"
png_female = "assets./female_user.png"
png_male = "assets./male_user.png"


def update_profile_pic(png):
    st.session_state["image"] = png
    


st.title("Login")
st.write("Faça o Login para acessar a Lojinha Online!")

with st.container():
    if "image" in st.session_state:
        st.image(st.session_state["image"],width=100)
    else:
        st.image(png_unknown,width=100)

    user = st.text_input('Usuario', 'Username')
    password = st.text_input('Senha', 'Password')

    login_but = st.button(
        label="Login", 
        help="Login do Usuário",
        on_click=update_profile_pic,
        kwargs={"png":"assets./female_user.png"}
    )

    st.markdown("Não possui uma conta ainda?")
    register_but= st.button(
        label="Register", 
        help="Registro de usuário",
        on_click=update_profile_pic,
        kwargs={"png":"assets./unknown_user.png"}
    )

if login_but:
    st.write("Login Feito!")
    
if register_but:
    st.write("Cadastrar usuário!")



def somar_dois(png):
    st.session_state["image"] = png

