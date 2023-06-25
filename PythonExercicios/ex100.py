from random import randint
from time import sleep

numeros = []


def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 100))
    print('Os números sorteados foram:', end=' ', flush=True)
    for n in numeros:
        print(n, end=' ', flush=True)
        sleep(0.6)
    print()
    print('-='*30)


def somaPar():
    soma_pares = 0
    cont_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            soma_pares += numero
            cont_pares += 1
    print(f'A soma dos {cont_pares} números pares é {soma_pares}')
    print('-='*30)


sorteia()
somaPar()
