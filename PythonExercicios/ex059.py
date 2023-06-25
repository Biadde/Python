# Menu de opções

menu = 0
print('-=-'*20)
n1 = int(input('Insere o 1º valor: '))
n2 = int(input('Insere o 2º valor: '))
print('-=-'*20)

while menu != 5:
    menu = int(input('''    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos números
    [5] Sair do programa
 Opção: '''))
    print('-=-'*20)

    if menu == 1:
        print(f'O resultado de {n1} + {n2} é \033[1;33m{n1 + n2}\033[m')
        print('-=-'*20)
    elif menu == 2:
        print(f'O reusultado de {n1} x {n2} é \033[1;33m{n1 * n2}\033[m')
        print('-=-'*20)
    elif menu == 3:
        if n1 > n2:
            print(f'O maior valor é o \033[1;33m{n1}\033[m')
            print('-=-'*20)
        if n1 == n2:
            print('Os dois valores são iguais')
            print('-=-'*20)
        if n1 < n2:
            print(f'O maior valor é o \033[1;33m{n2}\033[m')
            print('-=-'*20)

    elif menu == 4:
        n1 = int(input('Insere o 1º novo valor: '))
        n2 = int(input('Insere o 2º novo valor: '))
        print('-=-'*20)

    elif menu == 5:
        menu = 5
        print('Fim do programa! Volte sempre!')
        print('-=-'*20)

    else:
        print('\033[31mOpção Inválida. Tente Novamente!\033[m', )
        print('-=-'*20)
