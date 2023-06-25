print('-'*50)
numero_1 = int(input('Insere o 1º número: '))
numero_2 = int(input('Insere o 2º número: '))
numero_3 = int(input('Insere o 3º número: '))

# Verificar o menor número
if numero_1 < numero_2 and numero_1 < numero_3:
    menor = numero_1
if numero_2 < numero_1 and numero_2 < numero_3:
    menor = numero_2
if numero_3 < numero_1 and numero_3 < numero_2:
    menor = numero_3
print(f'O menor número é {menor}')

# Verificar o maior número
if numero_1 > numero_2 and numero_1 > numero_3:
    maior = numero_1
if numero_2 > numero_1 and numero_2 > numero_3:
    maior = numero_2
if numero_3 > numero_1 and numero_3 > numero_2:
    maior = numero_3
print(f'O maior número é {maior}')

print('-'*50)
