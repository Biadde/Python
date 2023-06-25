jogador = {}
golos = []
jogadores = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['jogos'] = int(input(f'Quantos jogos {jogador["nome"]} jogou?  '))
    jogador['golos'] = golos
    golos.clear()
    for partida in range(0, jogador['jogos']):
        golos.append(int(input(f'Quantos golos no {partida+1}º jogo: ')))
        jogador['golos'] = golos[:]   
    jogador['total'] = sum(golos)
    jogadores.append(jogador.copy())
    print('-='*30)
    continuar = str(input('Queres continuar[S/N]? ')).strip().upper()
    print('-='*30)
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar[S/N]? ')).strip().upper()
    if continuar == 'N':
        break

print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*75)

for k, v in enumerate(jogadores):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*75)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(jogadores):
        print(f'ERRO! Não existe nenhum jogador com o código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[busca]["nome"]}')
        for i, g in enumerate(jogadores[busca]['golos']):
            print(f'    No {i+1}º jogo, fez {g} golos')
    print('-='*30)
print('-='*30)
print('<< VOLTE SEMPRE >>')

