import random
from time import sleep

print('-=-'*15)
print('Jogo da advinhação')
print('-=-'*15)

print('Vou pensar em um número de \033[1;33m1\033[m a \033[1;33m10\033[m ...')
sleep(3)

tentativa = int(input('Em qual número pensei? '))
aleatorio = random.randint(1, 10)
contador = 1

while tentativa != aleatorio:
    contador += 1
    print('\033[1;31mErraste\033[m')
    tentativa = int(input('Tenta Novamente: '))

print(f'''\033[1;32mParabéns\033[m, pensei no número \033[1;33m{aleatorio}\033[m
Acertaste com \033[1;33m{contador}\033[m tentativas!''')
print('-'*45)