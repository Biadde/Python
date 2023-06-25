print('-'*50)
nome = input('Insere o teu nome completo: ').strip().title()
nome_silva = 'Silva' in nome

if nome_silva == True:
    print(f'Sim, {nome} tem "Silva" no nome')
else:
    print(f'Não, {nome} não tem "Silva" no nome')
print('-'*50)

