# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from gettext import install
from itertools import product
from turtle import position
import streamlit as st

st.image("assets./shopping_bag.png", width=75) 
st.title("Lojinha Online")

home, products, shop_kart, account = st.tabs(["Home", "Produtos", "Carrinho", "Conta"])
with home:
    # categorias de produtos da lojinha e destaques
    st.title("Home")
    st.image("assets./banner.png", width=700)
    st.image("assets./gaming.jpg", width=700)
    electronics, games, food = st.columns(3)

    with electronics:
        st.subheader("Eletrônicos")
        st.image("assets./electronics.png", width=200) 
        st.button("Veja mais em Eletrônicos")

    with games:
        st.subheader("Jogos")
        st.image("assets./games.png", width=200) 
        st.button("Veja mais em Jogos")

    with food:
        st.subheader("Comida")
        st.image("assets./food.png", width=200) 
        st.button("Veja mais em Comida")

with products:
    # todos os produtos da lojinha
    st.title("Todos os Produtos")
    col1, col2, col3 = st.columns(3)

    with col1:
        pass
    
    with col2:
        pass

    with col3:
        pass

with shop_kart:
    st.title("Carrinho")

    total= 100
    st.metric(label="Total", value=f'R${total}')

    # seleção da foma de pagamento
    with st.container():
        payment = st.selectbox(
        "Qual será a forma de pagamento?",
        ("Boleto", "Cartão de Crédito", "Crédito em conta"))

        # parcelamento se a opção selecionada for cartão de crédito
        if payment == "Cartão de Crédito":
            installments = st.selectbox(
            "Parcelamento",
            ("1x à vista", "2x sem juros", "3x sem juros", "4x sem juros", "5x sem juros", "6x sem juros", "12x sem juros"))
            
            match installments:
                case "1x à vista":
                    installments_opt = 1

                case "2x sem juros":
                    installments_opt = 2
                case "3x sem juros":
                    installments_opt = 3                
                case "4x sem juros":
                    installments_opt = 4
                case "5x sem juros":
                    installments_opt = 5                
                case "6x sem juros":
                    installments_opt = 6                
                case "12x sem juros":
                    installments_opt = 12

            st.metric(label="Valor Parcelado", value=f'{installments} de R${total/installments_opt}')

with account:
    # todos os produtos da lojinha
    st.title("Conta")
    col1, col2, col3 = st.columns(3)

    with col1:
        pass
    
    with col2:
        pass

    with col3:
        pass