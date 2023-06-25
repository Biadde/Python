print('\033[35m-=-'*20)
print('Analisador de médias')
print('-=-'*20,'\033[m')

nota1 = float(input('Insere a tua 1ª nota: %'))
nota2 = float(input('Insere a tua 2ª nota: %'))
media = (nota1 + nota2) / 2

print('-' * 50)
if media <= 50:
    print(f'Tens uma média de \033[1;31m{media:.2f}%\033[m\n\033[1mTens de estudar mais!\033[m')
elif media > 70:
    print(f'Parabéns! Tens uma média de \033[1;32m{media:.2f}%\033[m\n\033[1mContinua assim!\033[m')
else:
    print(f'Tens uma média de \033[1;33m{media:.2f}%\033[m\n\033[1mPodes melhorar!\033[m')
print('-'*50)
