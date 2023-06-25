from random import sample
from time import sleep

jogos = int(input('Quantos jogos queres que eu sorteie? '))
print(f'A SORTEAR {jogos} JOGOS...')
print('-='*30)
sleep(1)

for jogo in range(1, jogos+1):
    print(f'Jogo {jogo}:', end=' ')
    print(sorted(sample(range(0, 60), 6)))
    print()
    sleep(1)
print('-='*30)