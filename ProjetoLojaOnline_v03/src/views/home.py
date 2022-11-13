# Caio Rabinovich Panes Brunholi
# RA: 20.01285-3

import streamlit as st
from src.controllers.kart_controller import Kart
from src.models.product import Product
from src.controllers.product_controller import ProductController
from src.models.user import User
from src.controllers.user_controller import UserController


user_controller=UserController()
product_controller=ProductController()


if "hello" in st.session_state:
    st.session_state["hello"]
else:
    st.session_state["hello"]="Usuario(a)"

# DESCOMENTAR
# Criar carrinho
if "kart" not in st.session_state:
    st.session_state["kart"] = Kart()

# Importar todos os produtos do banco de dados
all_products = product_controller.pegar_todos_produtos()

def add_to_purchase(product_number_in_list):
    st.session_state["kart"].add_to_kart(all_products[product_number_in_list])

def remove_from_purchase(product_number_in_list):
    st.session_state["kart"].remove_from_kart(all_products[product_number_in_list])



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

        col1, col2 = st.columns(2)
        for n in range(len(all_products)):
            if (n % 2) == 0:
                with col1:
                    st.subheader(all_products[n].name)
                    st.image(all_products[n].image,width=150)
                    st.subheader(f'R${all_products[n].price}0')
                    st.caption(all_products[n].description)
                    st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_number_in_list":n}, key=n)
                    st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_number_in_list":n}, key=n+1000)
            else:
                with col2:
                    st.subheader(all_products[n].name)
                    st.image(all_products[n].image,width=150)
                    st.subheader(f'R${all_products[n].price}0')
                    st.caption(all_products[n].description)
                    st.button(label="Adicionar ao carrinho", on_click=add_to_purchase,kwargs={"product_number_in_list":n}, key=n)
                    st.button(label="Remover do carrinho", on_click=remove_from_purchase,kwargs={"product_number_in_list":n}, key=n+1000)



        st.header("Adicionar um novo produto")
        if "new_product" in st.session_state:
            st.session_state["new_product"]
        else:
            st.session_state["new_product"]=False

        def add_new_product(new_product_id, new_product_name, new_category, new_description, new_price, new_image):
            new_product = Product(id=new_product_id, name=new_product_name, category=new_category, description=new_description, price=new_price, image=new_image)
            print(new_product)
            success = product_controller.inserir_produto(new_product) 
            if success:
                print("Novo Produto Adicionado ao Banco de Dados")
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
            kwargs={"new_product_id":new_product_id, "new_product_name":new_product_name, "new_category":new_category, "new_description":new_description, "new_price":new_price, "new_image":new_image}
        )

        
        
        

    with shop_kart:
        st.title("Carrinho")

        #  Valores de teste
        # total = 100.0
        # n_items = 4
        total=st.session_state["kart"].get_total_value()
        n_items=st.session_state["kart"].get_quatity()
        st.metric(label="Itens no Carrinho", value=f'{n_items} itens')
        for n in range(n_items):
            st.info(st.session_state["kart"].get_item_in_array(n).name)
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
            st.header(st.session_state["hello"])
            st.metric(label="Credito da conta", value=f'R$211,50',delta='R$20,00')

        st.title("")
        st.title("Atualizar Dados de Conta")

        def update_user_database(logged_username, altered_email, altered_password):
            altered_user = user_controller.pegar_user(username=logged_username)
            if altered_user == None:
                st.write("Nome de Usuário Desconhecido")
            else:
                print(altered_user)
                altered_user.email = altered_email
                altered_user.password = altered_password
                print(altered_user)
                success = user_controller.atualizar_user(altered_user)
                if success:
                    print("Dados de usuario atualizado")
                    st.write(f"Os dados do usuário {altered_user.username} foram atualizados!")



        logged_username = st.text_input('Seu Nome de Usuário', 'Username')
        altered_email = st.text_input('Novo Endereço de Email', 'New Email')
        altered_password = st.text_input('Nova Senha', 'New Password')
        st.button(
            "Atualizar Dados",
            help="Finalizar atualização de dados",
            on_click=update_user_database,
            kwargs={"logged_username":logged_username, "altered_email":altered_email,"altered_password":altered_password}
        )
