print('-'*50)
nota1 = float(input('Insere a tua primeira nota: '))
nota2 = float(input('Insere a tua segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 50:
    print(f'\033[32mPARABÉNS! A tua média é de {media:.2f}%\033[m')
else:
    print(f'\033[31mDevias estudar mais! A tua média é de {media:.2f}%\033[m')
print('-'*50)