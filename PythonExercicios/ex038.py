print('\033[35m-=-'*15)
print('Comparador de números')
print('-=-'*15,'\033[m')
numero1 = int(input('Insere o 1º número: '))
numero2 = int(input('Insere o 2º número: '))
print('-'*50)

if numero1 > numero2:
    print(f'\033[1;33m{numero1}\033[m é maior do que \033[1;33m{numero2}\033[m')
elif numero2 > numero1:
    print(f'{numero2} é maior do que {numero1}')
else:
    print('\033[1;33mOs dois números são iguais!\033[m')
print('-'*50)
