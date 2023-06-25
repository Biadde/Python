print('-'*50)
distancia = int(input('Insere a distância da viagem em Km: '))

if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45

print(f'O preço de uma passagem de {distancia}Km será de {preço:.2f}€')
print('-'*50)
