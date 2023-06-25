from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('-=-'*20)
print(f'Os valores sorteados foram: \033[1;33m{numeros}\033[m')
print('-=-'*20)
print(f'O maior valor foi: \033[1;33m{sorted(numeros)[-1]}\033[m')
print(f'O menor valor foi: \033[1;33m{sorted(numeros)[0]}\033[m')
print('-=-'*20)