import moeda

preco = float(input('Insere o preço: €'))
aumento = int(input('Aumento do preço: %'))
dimi = int(input('Desconto do preço: %'))
print('-='*30)
print(f'A metade de {moeda.moeda(preco)} é {moeda.metade(preco, True)}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.dobro(preco, True)}')
print(f'Aumentando {aumento}% de {moeda.moeda(preco)} temos {moeda.aumentar(preco, aumento, True)}')
print(f'Reduzindo {dimi}% de {moeda.moeda(preco)} temos {moeda.diminuir(preco, dimi, True)}')
print('-='*30)
