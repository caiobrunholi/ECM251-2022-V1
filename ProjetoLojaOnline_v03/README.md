# Trabalho T4
## Nome:
#### Caio Rabinovich Panes Brunholi
#### RA: 20.01285-3
#

## Este README possui explicações de como utilizar esse programa
#
# Adição de novo Usuário
#### Na tela de Login use a opção "Register", e preencha os campos.
#### Não utilize ```usernames``` já presentes no banco de dados. São eles:
```
Fulana
Juninho
Marcia
Jackson
Fake
```


# Adição de Novo Produto
#### Role até o final da página "Produtos" e adicione o produto.
#### A imagem deve ser o caminho até o jpg ou png na pasta ```assets```.
``` 
EX:
"assets./exemple_image.png"
```
#### Uma imagem com o nome acima já está incluída na pasta, caso queira usar.
#### Para evitar conflitos com os itens já existentes utilize um id inferior a 10000 ou superior a 40000.
# Alteração de Dados de Usuário
#### Role até o final da página "Conta" e modifique a conta de usuário desejada.
#### Para fazer a alteração é necessário fornecer um username existente no banco de dados, alguns já inclusos são:
```
Fulana
Juninho
Marcia
Jackson
Fake
```
# Para rodar
#### Para rodar o sistema utilizar os comandos:
```
cd Scripts
activate
cd ..
python -m streamlit run ./src/main.py
```
# Solução de Problemas
#### O carrinho ```"kart"``` pode não ser iniciado corretamente pelo ```streamlit```, infelizmente parece ser um problema da biblioteca ou do ```st.session_state```.
#### A solução caso encontre esse problema é...
```
Parar o programa e rodar novamente 
ou 
Dar um refresh na página

¯\_(ツ)_/¯
```

# 


```
|-----------|
| ENFIM,    |
| É         |
| ISSO.     |
| OBRIGADO! |
|-----------|
(\__/) ||
(•ㅅ•) ||
/ 　 づ

CB
```