soma = 0
cont = 0

for numero in range(1, 501, 2):
    if numero % 3 == 0:
        cont = cont + 1
        soma = soma + numero
print(f'A soma de todos os \033[1m{cont}\033[m valores solicitados é \033[1;33m{soma}\033[m')
