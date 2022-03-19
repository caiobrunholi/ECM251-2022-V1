# **REQUISITOS DO PROJETO ANUAL**

# **Anotações de Visual** 

### **UX and UI**
Devem se basear em plataformas já existentes, como:
    - Steam
    - Nuuvem
    - Origin 

### **Descritos Pelo Cliente**
- Comprar Jogos
- Devolução/Reembloso de Jogos 
    - Prazo máximo de arrependimento: 7 dias
- Perfis individuais de Jogos
    - Área de Feedback
        - Somente quem possui o Jogo pode fornecer Feedback
- Sistema de Troféis 

### **Observado nas Referências**
- Home
    - Promoções
    - Principais Jogos 
    - Login
    - Instalar programa no PC
- Pesquisar Jogos
    - Pesquisar Jogos por categorias / Filtros
- Categorias
    - Tipos e Jogos 
    - Plataformas (PC, Console, Mobile) 
    - Publishers
- Perfil
    - Conta
    - Carrinho 
    - Dados do Usuário
- Comunidade
    - Discussão por jogos
        - Perfil de Jogos 
    - Notas
        - Perfil de Jogos
    - Trade de Itens
        - Perfil de Jogos 


<br/><br/>

# **Uso e Funcionalidade**

### **Navegação**
- Conta no canto superior direito
    - Ao clicar leva à pagina de perfil
- Carrinho dp lado esquerdo da conta 
- Logo do Site no canto superior direito
    - Ao clicar leva à Home

### **Conta**
- Criação de Conta
    - Pede dados do usuário
    - Email de Recuperação
    - Verifição de duas etapas
        - Telefone
- Dados do Usuário
    - Nome
    - Data de Nascimento
    - País
    - Email
    - Telefone 
    - Método de Pagamento
        - Cartão de Crédito 
            - Nome no Cartão
            - Numero do Cartão
            - Valido até
            - Bandeira
            - CVV
        - Gift Card
            - Número do Cartão
- Saldo em conta
- Meus Produtos 
    - Jogos
        - Troféus
        - Horas Jogadas
    - Itens de Jogos

### **Perfil**
- Vizualização de Jogos do Usuário *(Público)*
     - Instalar/Desinstalar Jogo *(Privado)*
        - Botão do lado do nome do Jogo
    - Horas jogadas *(Público)*
        - Abaixo de Nome e Logo do Jogo
    - Troféus de cada Jogo *(Público)*
        - Abaixo de horas jogadas
    - Itens comprados nos jogos *(Privado)*
        - Abaixo de Troféus

- Configurações da conta *(Privado)*
    - Canto Superior

### **Carrinho**
- Selecionar Jogos
- Selecionar Itens
- Método de Pagamento
    - Cartão de Crédito
    - Saldo em conta (Gift Cards)

### **Pesquisa**
- Centrado no topo da página
- Nome do Jogo
- Categorias de Jogos
- Itens 
- Após pesquisa
    - Barra Lateral
        - Filtros
            - Preço
            - Categorias
            - Avaliação 


### **Jogos**
- Nome do Jogo
- Horas Jogadas
- Troféus 
- Itens para compra
- Nota
- Avaliações 

### **Itens**
- Nome do item 
- Jogo de qual pertence
- Descrição 
    - Tipo de item
    - Habilidades Especiais
    - Texto de apresentação

### **Comunidade**
- Dividida por jogos 
    - Nome do Jogo
        - Nota
        - Comentários 
            - O usuário possui o jogo?
            - Sim
                - Pode dar nota e adicionar comentário
            - Não
                - Pode somente vizualizar



<br/><br/>

# **Classes**

## **User**
- Nome *(String)*
- Data de Nascimento *(String)*
- País *(String)*
- Email *(String)*
- Telefone *(int)*
- Método de Pagamento
    - Cartão de Crédito 
        - Nome no Cartão *(String)*
        - Numero do Cartão *(int)*
        - Valido até 
            - Mês *(int)*
            - Ano *(int)*
        - Bandeira *(String)*
        - CVV *(int)*
    - Gift Card
        - Número do Cartão *(int)*
- Saldo em conta *(double)*
- Jogos 
    - Nome *(String)*
    - Horas Jogadas *(double)*
    - Troféus *(String)*
- Itens 
    - Nome *(String)*
    - Jogo *(String)*



## **Jogo**
- Nome do Jogo *(String)*
- Categoria
- Desenvolvedor/Publisher *(String)*
- Data de Lançamento *(String)*
- Troféus *(String)*
- Itens para compra *(String)*
- Nota *(int)*
- Avaliações *(String)*
- Valor *(double)*

## **Item**
- Nome *(String)*
- Jogo *(String)*
- Descrição 
    - Tipo de item *(String)*
    - Habilidades Especiais *(String)*
    - Texto de apresentação *(String)*
- Valor *(double)*


## **Comunidade**
- Jogo *(String)*
- Participantes
    - Nome *(String)*
    - Quantidade *(int)*









