from datetime import date

print('\033[35m-=-'*15)
print('Alistamento Militar')
print('-=-'*15, '\033[m')

ano = int(input('Insere o teu ano de nascimento: '))
idade = date.today().year - ano

if idade < 18:
    tempo_falta = 18 - idade
    print(f'Faltam \033[1;33m{tempo_falta}\033[m anos para o teu alistamento militar.')
elif idade == 18:
    print('\033[1;33mO teu alistamento militar é este ano.\033[m')
elif idade > 18:
    tempo_passou = idade - 18
    print(f'O teu alistamento militar foi há \033[1;33m{tempo_passou}\033[m atrás.')
print('-'*50)