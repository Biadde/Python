print('\033[35m-=-'*15)
print('Calculadora de IMC')
print('-=-'*15, '\033[m')

peso = float(input('Insere o teu peso(Kg): '))
altura = float(input('Insere a tua altura(m): '))
imc = peso / (altura**2)

print('-'*50)

if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
elif imc >= 40:
    print('Obesidade Mórbida')

print('-'*50)