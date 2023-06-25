from utilidades import dado, moeda

preco = dado.leiaDinheiro('Insere o preço: €')
aumento = dado.leiaInt('Aumento do preço: %')
dimi = dado.leiaInt('Desconto do preço: %')
moeda.resumo(preco, aumento, dimi)
