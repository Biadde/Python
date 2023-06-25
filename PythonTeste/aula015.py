n = 0
soma = 0

while True:
    n = int(input('Insere um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma é {soma}')