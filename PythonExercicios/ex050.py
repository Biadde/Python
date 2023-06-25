soma = 0

for n in range(1, 7):
    numero = int(input('Insere um número: '))
    if numero % 2 == 0:
        soma = soma + numero
print(f'A soma de todos os números pares inseridos é {soma}')
