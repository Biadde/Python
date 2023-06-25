print('-'*50)
salario = int(input('Insere o salário do funcionário: '))

if salario > 1250:
    aumento = salario * 10 / 100
else:
    aumento = salario * 15 / 100

salario_final = salario + aumento

print(f'Com um salário de {salario}€,\nO seu aumento será de: {aumento:.2f}€\nO novo salário do funcionário será de: {salario_final:.2f}€')
print('-'*50)