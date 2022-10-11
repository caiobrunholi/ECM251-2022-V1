# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from email.mime import image
import streamlit as st
from src.controllers.kart_controller import Kart
from src.controllers.product_controller import ProductController

# NAO CONSIGO FAZER BOTAO IR PARA OUTRA ST.TAB


kart1 = Kart()
all_products = ProductController()

def show_home_page():
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
            st.subheader(all_products.products[0].name)
            st.image(all_products.products[0].image,width=150)
            st.subheader(f'R${all_products.products[0].price},00')
            st.caption(all_products.products[0].desciption)

            st.subheader(all_products.products[3].name)
            st.image(all_products.products[3].image,width=150)
            st.subheader(f'R${all_products.products[3].price},00')
            st.caption(all_products.products[3].desciption)

            st.subheader(all_products.products[6].name)
            st.image(all_products.products[6].image,width=150)
            st.subheader(f'R${all_products.products[6].price},00')
            st.caption(all_products.products[6].desciption)

            st.subheader(all_products.products[9].name)
            st.image(all_products.products[9].image,width=150)
            st.subheader(f'R${all_products.products[9].price},00')
            st.caption(all_products.products[9].desciption)
        
        
        
        
        with col2:
            st.subheader(all_products.products[1].name)
            st.image(all_products.products[1].image,width=150)
            st.subheader(f'R${all_products.products[1].price},00')
            st.caption(all_products.products[1].desciption)

            st.subheader(all_products.products[4].name)
            st.image(all_products.products[4].image,width=150)
            st.subheader(f'R${all_products.products[4].price},00')
            st.caption(all_products.products[4].desciption)

            st.subheader(all_products.products[7].name)
            st.image(all_products.products[7].image,width=150)
            st.subheader(f'R${all_products.products[7].price},00')
            st.caption(all_products.products[7].desciption)

            st.subheader(all_products.products[10].name)
            st.image(all_products.products[10].image,width=150)
            st.subheader(f'R${all_products.products[10].price},00')
            st.caption(all_products.products[10].desciption)
        
        
        

        with col3:
            st.subheader(all_products.products[2].name)
            st.image(all_products.products[2].image,width=150)
            st.subheader(f'R${all_products.products[2].price},00')
            st.caption(all_products.products[2].desciption)

            st.subheader(all_products.products[5].name)
            st.image(all_products.products[5].image,width=150)
            st.subheader(f'R${all_products.products[5].price},00')
            st.caption(all_products.products[5].desciption)

            st.subheader(all_products.products[8].name)
            st.image(all_products.products[8].image,width=150)
            st.subheader(f'R${all_products.products[8].price},00')
            st.caption(all_products.products[8].desciption)
        
        
        

    with shop_kart:
        st.title("Carrinho")

        # total= 100
        total=kart1.get_total_value()
        n_items=kart1.get_quatity()
        st.metric(label="Itens no Carrinho", value=f'{n_items} itens')
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
            st.markdown("### Dados da Conta")
            st.markdown("")
            st.markdown("### Métodos de Pagamento")
            st.markdown("")
            st.markdown("### Adicionar Crédito à Conta")
            st.markdown("")
            st.markdown("### Compras Anteriores")
            st.markdown("")
            st.markdown("### Devoluções")
        
        with col2:
            pass

        with col3:
            st.image("assets./female_user.png")
            st.header("Fulana")
            st.metric(label="Credito da conta", value=f'R$211,50',delta='R$20,00')
