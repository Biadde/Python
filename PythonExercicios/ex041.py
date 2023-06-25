from datetime import date

print('\033[35m-=-'*15)
print('Escalões de atletas')
print('-=-'*15 ,'\033[m')

ano = int(input('Insere o ano de nascimento do atleta: '))
idade = date.today().year - ano

print('-'*50)
print(f'O atleta tem {idade} anos')
if idade < 10:
    print('Escalão: \033[1;33mMinis A\033[m')
elif idade >= 10 and idade <= 12:
    print('Escalão: \033[1;33mMinis B\033[m')
elif idade == 13:
    print('Escalão: \033[1;33mInfantis\033[m')
elif idade == 14:
    print('Escalão: \033[1;33mIniciados\033[m')
elif idade == 15 or idade == 16:
    print('Escalão \033[1;33mJuvenis\033[m')
elif idade == 17:
    print('Escalão: \033[1;33mJuniores\033[m')
else:
    print('Escalão: \033[1;33mSêniores\033[m')
print('-'*50)
