def leiaInt(a):
    while True:
        n = str(input(a))
        if not n.isnumeric():
            print('\033[31mERRO! Insere um número inteiro válido.\033[m')
        else:
            valor = int(n)
            break
    return valor


romana = []
print('-='*20)
print('Conversor de números romanos'.center(40))
print('-='*20)
while True:
    num = leiaInt('Insere um número: ')
    n = num
    while n > 0:
        if n >= 10:
            romana.append('X')
            n = n - 10
        elif n == 9:
            romana.append('IX')
            n = n - 9
        elif n < 10 and n >= 5:
            romana.append('V')
            n = n - 5
        elif n == 4:
            romana.append('IV')
            n = n - 4
        else:
            romana.append('I')
            n = n - 1
    print(f'O número {num} convertido fica ', end='')
    for l in romana:
        print(l, end='')
    print()
    romana.clear()
    print('-'*30)
    continuar = input('Queres continuar?[S/N] ').strip().upper()
    print('-'*30)
    while 'S' not in continuar and 'N' not in continuar:
        print('\033[1;31mResposta Inválida!\033[m')
        continuar = input('Queres continuar?[S/N] ').strip().upper()
    if continuar == 'N':
        break

