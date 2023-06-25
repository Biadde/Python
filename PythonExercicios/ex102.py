def fatorial(num, show=False):
    '''--> Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n'''

    print('-'*30)
    print(f'!{num} =', end=' ')
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        f *= c
    return f


n = int(input('Insere um número: '))
print(fatorial(n, True))
