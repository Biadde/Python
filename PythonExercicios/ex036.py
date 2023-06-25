from datetime import date

print('\033[33m-=-'*25)
print('Aprovador de empréstimos')
print('-=-'*25,'\033[m')

casa = int(input('Insere o valor da casa: €'))
salario = int(input('Insere o teu salário: €'))
anos = int(input('Insere a quantidade de anos que desejas parcelar a casa: '))
prestação = casa / (anos * 12)

print('-'*50)

if prestação > salario * (30 / 100):
    print(f'Para pagar uma casa de {casa}€ em {anos} anos a prestaçao será de {prestação:.2f}€')
    print('\033[31mInfelizmente, não podemos aceitar o teu empréstimo!\033[m')
else:
    final = date.today().year + anos
    print(f'\033[32mEmpréstimo aceito!\033[m\nA tua casa estará paga em \033[1m{final}\033[m\nTerá um custo de \033[1;33m{prestação:.2f}€\033[m por mês')
print('-'*50)
