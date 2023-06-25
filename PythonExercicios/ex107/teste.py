import moeda

preco = float(input('Insere o preço: €'))
aumento = int(input('Aumento do preço: %'))
dimi = int(input('Desconto do preço: %'))
print(f'A metade de {preco} é {moeda.metade(preco)}')
print(f'O dobro de {preco} é {moeda.dobro(preco)}')
print(f'Aumentando {aumento}% de {preco}, temos {moeda.aumentar(preco, aumento)}€')
print(f'Reduzindo {dimi}% de {preco}, temos {moeda.diminuir(preco, dimi)}€')
