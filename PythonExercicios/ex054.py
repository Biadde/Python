from datetime import date

print('-=-'*15)
print('Grupo da Maioridade')
print('-=-'*15)

maiores = 0
menores = 0

for vezes in range(1, 8):
    nascimento = (int(input(f'Em que ano a {vezes}ª pessoa nasceu? ')))
    print('-'*45)

    idade = date.today().year - nascimento

    if idade >= 18:
        maiores = maiores + 1
    else: 
        menores = menores + 1
print(f'Há \033[1;32m{maiores}\033[m maior(es) de idade e \033[1;31m{menores}\033[m menor(es) de idade no grupo')
