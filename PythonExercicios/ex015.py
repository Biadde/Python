print('-'*50)
dias = int(input('Insere por quantos dias o carro foi alugado: '))
km = float(input('Insere quantos Km percorreu com o carro: '))

preço = (dias* 60) + (km * 0.15)

print(f'O preço a pagar por o aluguel de {dias} dias e por {km}Km rodados é: {preço}€ ')
print('-'*50)