from random import choice
print('-'*50)
aluno1 = input('Insere o nome do 1º aluno: ')
aluno2 = input('Insere o nome do 2º aluno: ')
aluno3 = input('Insere o nome do 3º aluno: ')
aluno4 = input('Insere o nome do 4º aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]

print(f'O aluno escolhido foi: {choice(lista)}')
print('-'*50)
