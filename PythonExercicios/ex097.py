def escreva(a):
    msg = f'  {a}  '
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))


escreva(str(input('Escreve uma frase: ')))