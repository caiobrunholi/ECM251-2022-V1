from modelos.produtos.item import Item
from modelos.carrinho.carrinho import Carrinho

item1=Item('Carregador','Carrega iPhone e Android',200.0)

item2 = Item(
    valor=350.0,
    nome='Stray',
    descricao='gato'
)

item3 = Item(
    valor=350.0,
    nome='Stray',
    descricao='gato'
)

carrinho=Carrinho()
print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.adicionar(item1)
carrinho.adicionar(item2)

print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

# print(item1 == item2)
# print(item1 == item1)
# print(item2 == item3)

carrinho.remover(item1)
print(f'Tamanho: {carrinho.get_quantidade_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')