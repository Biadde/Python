from random import randint
from time import sleep

print('-'*50)
print('Vou pensar em um número de 1 a 5...')
numero = randint(1, 5)
sleep(1)
tentativa = int(input('Em qual número pensei? '))

if tentativa == numero:
    print(f'PARABÉNS! Eu pensei no número {numero}')
else:
    print(f'ERRASTE! Eu pensei no número {numero}')
print('-'*50)