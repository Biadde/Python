lista = []
soma = 0
for a in range(0, 4):
    lista.append(float(input(f'{a+1}ª nota: ')))
    soma += lista[a]
print(f'A média final é de {soma / 4:.2f}%')
print(f'A maior nota foi {max(lista):.2f}% e a menor nota foi {min(lista):.2f}%')