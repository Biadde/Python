def leiaInt(a):
    while True:
        n = str(input(a))
        if not n.isnumeric():
            print('\033[31mERRO! Insere um número inteiro válido.\033[m')
        else:
            valor = int(n)
            break
    return valor


n = leiaInt('Insere um número: ')
print(f'Acabaste de inserir o número {n}')
