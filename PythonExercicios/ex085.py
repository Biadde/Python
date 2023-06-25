lista = [[], []]

for a in range(1, 8):
    n = (int(input(f'Insere o {a}º valor: ')))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)

print('-='*30)
print(f'Os valores pares inseridos foram: {sorted(lista[0])}')
print(f'Os valores ímpares inseridos foram: {sorted(lista[1])}')
print('-='*30)