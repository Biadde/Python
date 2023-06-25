import moeda

preco = float(input('Insere o preço: €'))
aumento = int(input('Aumento do preço: %'))
dimi = int(input('Desconto do preço: %'))
print('-='*30)
print(f'A metade de {moeda.moeda(preco)} é {moeda.moeda(moeda.metade(preco))}')
print(f'O dobro de {moeda.moeda(preco)} é {moeda.moeda(moeda.dobro(preco))}')
print(f'Aumentando {aumento}% de {moeda.moeda(preco)} temos {moeda.moeda(moeda.aumentar(preco, aumento))}')
print(f'Reduzindo {dimi}% de {moeda.moeda(preco)} temos {moeda.moeda(moeda.diminuir(preco, dimi))}')
print('-='*30)
