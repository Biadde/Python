print('-'*50)
velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'FOSTE MULTADO! O limite de velocidade são 80Km/h\nO valor da multa é de: {multa}€ ')
else:
    print(f'Muito bem! Vais dentro dos limites de velocidade!')
print('-'*50)
