def ficha(nome, golos):
    print('-'*60)
    if nome == '':
        nome = '<desconhecido>'
    if golos == '':
        golos = 0
    print(f'O jogador {nome} marcou {golos} golo(s) no campeonato.')
    return nome, golos


print('-'*60)
n = str(input('Insere o nome do jogador: ')).capitalize().strip()
g = input('Insere a quantidade de golos marcados: ').strip()


ficha(n, g)
