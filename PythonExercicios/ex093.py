jogador = {}
golos = []

jogador['nome'] = str(input('Nome do jogador: '))
jogador['jogos'] = int(input(f'Quantos jogos {jogador["nome"]} jogou?  '))

for partida in range(0, jogador['jogos']):
    golos.append(int(input(f'Quantos golos no {partida+1}º jogo: ')))
    jogador['golos'] = golos[:]   
jogador['total'] = sum(golos)
print('-='*30)
print(jogador)
print('-='*30)

for k, v in jogador.items():
    print(f'{k} tem o valor {v}')
print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {jogador["jogos"]} jogos')

for jogo in range(0, jogador['jogos']):
    print(f'   - No {jogo+1}º jogo, marcou {jogador["golos"][jogo]} golos')
print(f'Foi um total de {jogador["total"]} golos')