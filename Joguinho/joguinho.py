from random import randint
from time import sleep
pontuacao_total = 0

continuar = 'S'
while 'S' in continuar:
    computador = randint(1, 10)
    jogador = 0
    tentativas = 5
    pontuacao = 0

    print('Vou pensar em um número de 1 a 10...')
    sleep(1.5)
    try:
        while tentativas > 0 and computador != jogador:
            jogador = int(input('Em qual número pensei? '))
            tentativas -= 1
            if computador != jogador and tentativas > 0:
                print('-=' * 30)
                print(f'\033[1;31mErraste!\033[m Tens \033[1;33m{tentativas}\033[m tentativas restantes')
            print('-='*30)
    except ValueError:
        print('Valor inválido! Tenta novamente')
        while tentativas > 0 and computador != jogador:
            jogador = int(input('Em qual número pensei? '))
            tentativas -= 1
            if computador != jogador and tentativas > 0:
                print('-=' * 30)
                print(f'\033[1;31mErraste!\033[m Tens \033[1;33m{tentativas}\033[m tentativas restantes')
            print('-=' * 30)

    if computador == jogador:
        if tentativas == 4:
            pontuacao += 100
        elif tentativas == 3:
            pontuacao += 70
        elif tentativas == 2:
            pontuacao += 50
        elif tentativas == 1:
            pontuacao += 20
        elif tentativas == 0:
            pontuacao += 10
        pontuacao_total += pontuacao
        print(f'\033[1;32mParabéns!\033[m Acertaste com \033[1;33m{5-tentativas}\033[m tentativas')
    else:
        if tentativas == 0:
            print('\033[1;31mPerdeste! Acabaram as tuas tentativas\033[m')
    print(f'+ {pontuacao} pontos')
    print('-='*30)
    continuar = str(input('Queres jogar novamente?[S/N] ')).strip().upper()
    while 'S' not in continuar and 'N' not in continuar:
        print('\033[1;31mResposta Inválida! Tenta novamente\033[1;31m')
        continuar = str(input('Queres jogar novamente?[S/N] ')).strip().upper()
    print('-='*30)
    if 'N' in continuar:
        break
print(f'A tua pontuação final é de \033[1;33m{pontuacao_total}\033[m pontos')