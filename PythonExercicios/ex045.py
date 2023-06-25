import random

print('-=-'*20)
jogador = str(input('\033[35mVamos jogar!\033[m\nEscolhe um: \033[1mPedra\033[m, \033[1mpapel\033[m ou \033[1mtesoura\033[m: ').lower().strip())
lista = ['pedra', 'papel', 'tesoura']
computador = random.choice(lista)
print('-=-'*20)
# Condições se o jogador escolher pedra
if jogador == 'pedra' and computador == 'pedra':
    print('\033[1;33mNinguém ganhou!\033[m')
elif jogador == 'pedra' and computador == 'papel':
    print('\033[1;31mPerdeste!\033[m')
elif jogador == 'pedra' and computador == 'tesoura':
    print('\033[1;32mGanhaste!\033[m')

# Condições se o jogador escolher papel
if jogador == 'papel' and computador == 'pedra':
    print('\033[1;32mGanhaste!\033[m')
elif jogador == 'papel' and computador == 'papel':
    print('\033[1;33mNinguém ganhou!\033[m')
elif jogador == 'papel' and computador == 'tesoura':
    print('\033[1;31mPerdeste!\033[m')

# Condições se o jogador escolher tesoura
if jogador == 'tesoura' and computador == 'pedra':
    print('\033[1;31mPerdeste!\033[m')
elif jogador == 'tesoura' and computador == 'papel':
    print('\033[1;32mGanhaste!\033[m')
elif jogador == 'tesoura' and computador == 'tesoura':
    print('\033[1;33mNinguém ganhou!\033[m')

print(f'Eu escolhi: {computador.capitalize()}')
print('-'*50)