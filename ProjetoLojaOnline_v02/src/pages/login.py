from cProfile import label
from turtle import onclick
import streamlit as st


st.title("Login")
st.write("Faça o Login para acessar a Lojinha Online!")

user = st.text_input('Usuario', 'Username')
password = st.text_input('Senha', 'Password')

loginbut = st.button("Login!")

