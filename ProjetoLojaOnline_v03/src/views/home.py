# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

from email.mime import image
import streamlit as st
from src.controllers.kart_controller import Kart
from src.controllers.product_controller import ProductController

# NAO CONSIGO FAZER BOTAO IR PARA OUTRA ST.TAB

if "kart" not in st.session_state:
    st.session_state["kart"] = Kart()
all_products = ProductController()

def add_to_purchase(product_id):
    st.session_state["kart"].add_to_kart(all_products.products[product_id])

def remove_from_purchase(product_id):
    st.session_state["kart"].remove_from_kart(all_products.products[product_id])


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
            st.button("Veja mais em Eletrônicos") #Comando ainda não implementado

        with games:
            st.subheader("Jogos")
            st.image("assets./games.png", width=200) 
            st.button("Veja mais em Jogos") #Comando ainda não implementado

        with food:
            st.subheader("Comida")
            st.image("assets./food.png", width=200) 
            st.button("Veja mais em Comida") #Comando ainda não implementado

    with products:
        # todos os produtos da lojinha
        st.title("Todos os Produtos")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.subheader(all_products.products[0].name)
            st.image(all_products.products[0].image,width=150)
            st.subheader(f'R${all_products.products[0].price},00')
            st.caption(all_products.products[0].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":0}, key=1000)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":0}, key=2000)

            st.subheader(all_products.products[3].name)
            st.image(all_products.products[3].image,width=150)
            st.subheader(f'R${all_products.products[3].price},00')
            st.caption(all_products.products[3].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":3}, key=1003)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":3}, key=2003)

            st.subheader(all_products.products[6].name)
            st.image(all_products.products[6].image,width=150)
            st.subheader(f'R${all_products.products[6].price},00')
            st.caption(all_products.products[6].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":6}, key=1006)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":6}, key=2006)

            st.subheader(all_products.products[9].name)
            st.image(all_products.products[9].image,width=150)
            st.subheader(f'R${all_products.products[9].price},00')
            st.caption(all_products.products[9].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":9}, key=1009)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":9}, key=2009)

        
        
        
        
        with col2:
            st.subheader(all_products.products[1].name)
            st.image(all_products.products[1].image,width=150)
            st.subheader(f'R${all_products.products[1].price},00')
            st.caption(all_products.products[1].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":1}, key=1001)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":1}, key=2001)


            st.subheader(all_products.products[4].name)
            st.image(all_products.products[4].image,width=150)
            st.subheader(f'R${all_products.products[4].price},00')
            st.caption(all_products.products[4].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":4}, key=1004)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":4}, key=2004)


            st.subheader(all_products.products[7].name)
            st.image(all_products.products[7].image,width=150)
            st.subheader(f'R${all_products.products[7].price},00')
            st.caption(all_products.products[7].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":7}, key=1007)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":7}, key=2007)


            st.subheader(all_products.products[10].name)
            st.image(all_products.products[10].image,width=150)
            st.subheader(f'R${all_products.products[10].price},00')
            st.caption(all_products.products[10].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":10}, key=1010)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":10}, key=2010)

        
        
        

        with col3:
            st.subheader(all_products.products[2].name)
            st.image(all_products.products[2].image,width=150)
            st.subheader(f'R${all_products.products[2].price},00')
            st.caption(all_products.products[2].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":2}, key=1002)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":2}, key=2002)

            st.subheader(all_products.products[5].name)
            st.image(all_products.products[5].image,width=150)
            st.subheader(f'R${all_products.products[5].price},00')
            st.caption(all_products.products[5].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":5}, key=1005)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":5}, key=2005)


            st.subheader(all_products.products[8].name)
            st.image(all_products.products[8].image,width=150)
            st.subheader(f'R${all_products.products[8].price},00')
            st.caption(all_products.products[8].desciption)
            st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_id":8}, key=1008)
            st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_id":8}, key=2008)

        st.header("Adicionar um novo produto")
        if "new_product" in st.session_state:
            st.session_state["new_product"]
        else:
            st.session_state["new_product"]=False
        def add_new_product():
            st.write("Novo Produto Adicionado ao Banco de Dados")

        new_product_id = st.text_input('ID do produto', 000)
        new_product_name = st.text_input('Nome do novo produto', 'Product name')
        new_category = st.text_input('Categoria do novo produto', 'Category')
        new_description = st.text_input('Descrição do novo produto', 'Description')
        new_price = st.text_input('Preço do novo produto', 00.00) 
        new_image = st.text_input('Imagem do novo produto', "assets./example_image.png") 
        add_to_datebase_but = st.button(
            label="Adicionar Novo Produto", 
            help="Adicionar",
            on_click=add_new_product,
            kwargs={}
        )

        
        
        

    with shop_kart:
        st.title("Carrinho")

        total=st.session_state["kart"].get_total_value()
        n_items=st.session_state["kart"].get_quatity()
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
            
            buy_but = st.button("Pagar") # Não implementado nessa versão

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
