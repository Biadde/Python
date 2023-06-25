n = 0
soma = 0
c = 0

while n != 999:
    n = int(input('Insere um número: '))
    print('-'*50)
    if n != 999:
        soma += n
        c += 1

print(f'A soma de todos os \033[1m{c}\033[m números inseridos é \033[1;33m{soma}\033[m')
print('-'*50)
