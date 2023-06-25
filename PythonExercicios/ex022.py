print('-'*50)
nome = str(input('Insere o teu nome completo: ')).strip()
print('-'*50)
lista = nome.split()
nome_sem_espaco = "".join(lista)

print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
print(f'No total o nome {nome} tem: {len(nome_sem_espaco)} letras')
print(f'O teu primeiro nome é {lista[0]} e ele tem: {len(lista[0])} letras')
print('-'*50)

