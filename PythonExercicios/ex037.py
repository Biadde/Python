print('\033[35m-=-'*20)
print('Conversor de Bases Numéricas')
print('-=-'*20, '\033[m')

numero = int(input('Insere um número inteiro: '))
print('''Escolhe uma das bases para conversão:
[1] converter para \033[1mbinário\033[m
[2] converter para \033[1moctal\033[m
[3] converter para \033[1mhexadecimal\033[m''')
opçao = int(input('Opção: '))

if opçao == 1:
    print(f'\033[1m{numero}\033[m convertido para binário é igual a \033[1;33m{bin(numero)[2:]}\033[m')
elif opçao == 2:
    print(f'\033[1m{numero}\033[m convertido para octal é igual a \033[1;33m{oct(numero)[2:]}\033[m')
elif opçao == 3:
    print(f'\033[1m{numero}\033[m convertido para hexadecimal é igual a \033[1;33m{hex(numero)[2:]}\033[m')
else:
    print('\033[1;31mOpção Inválida!\nTente Novamente\033[m')