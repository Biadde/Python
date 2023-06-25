preço = float(input('Insere o preço do produto: €'))
desconto = float((input('Insere o desconto do produto: %')))
print('-' * 70)
preço_poupado = preço * desconto / 100
preço_final = preço - preço_poupado

print(f'Um produto que custe {preço}€ e tenha {desconto}% de desconto irá custar {preço_final:.2f}€')
print('-' * 70)