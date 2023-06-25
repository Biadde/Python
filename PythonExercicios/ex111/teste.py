from utilidades import moeda

preco = float(input('Insere o preço: €'))
aumento = int(input('Aumento do preço: %'))
dimi = int(input('Desconto do preço: %'))
moeda.resumo(preco, aumento, dimi)
