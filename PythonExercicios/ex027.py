print('-'*60)
nome = input('Insere o teu nome completo: ').strip().title()
nome_separado = nome.split()
numero_palavras = nome.count(' ')

print(f'Primeiro nome: {nome_separado[0]}')
print(f'Último nome: {nome_separado[numero_palavras]}')
print('-'*60)