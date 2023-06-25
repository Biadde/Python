from random import randint
from time import sleep

print('-=-'*20)
print('Vamos jogar par ou ímpar!')
print('-=-'*20)

computador = randint(1, 10)
vitórias = 0
derrotas = 0
continuar = 'S'

while True:
    n = int(input('\033[1mInsere um valor: \033[m'))
    resp = str(input('\033[1mPar ou Ímpar? [P/I]: \033[m')).strip().upper()
    print('-'*40)

# Condicao para só aceitar de resposta o 'P' ou o 'I'
    while 'P' not in resp and 'I' not in resp:
        resp = str(input('\033[31mResposta Inválida. Tente Novamente [P/I]:\033[m')).strip().upper()

    total = n + computador

    print(f'Tu jogaste {n} e o computador {computador}')
    print(f'Tu escolheste {resp} e {total} é ', end='')
    if total % 2 == 0:                # Condicao para saber se é par
        numero = True
        print('\033[1;33mPAR\033[m')
    else:                             # Condicao para saber se é impar
        print('\033[1;33mÍMPAR\033[m')
        numero = False
    print('-'*45)

# Condições para ganhar
    if resp == 'P' and numero == True:
        vitórias += 1
        print('\033[1;32mGANHASTE!\033[m')

    elif resp == 'I' and numero == False:
        vitórias += 1
        print('\033[1;32mGANHASTE!\033[m')

      
# Condições para perder
    elif resp == 'P' and numero == False:
        derrotas += 1
        print('\033[1;31mPERDESTE!\033[m')

    elif resp == 'I' and numero == True:
        derrotas += 1
        print('\033[1;31mPERDESTE!\033[m')

    sleep(1)
    continuar = str(input('\033[1mVamos jogar novamente?[S/N]: \033[m')).strip().upper()
    while continuar != 'S' and continuar != 'N':
        continuar = str(input('\033[31mResposta Inválida. Tente Novamente [S/N]:\033[m ')).strip().upper()


# Condição para acabar o loop
    if continuar == 'N':
        break
print('-=-' * 20)
print(f'\033[35mGAME OVER!\033[m Tu ganhaste \033[1;33m{vitórias}\033[m vezes.')
print('-=-'*20)
