matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = 0
soma3c = 0
maior = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Insere um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if c == 2:
            soma3c += matriz[l][c]
        if l == 1:
            if c == 0:
                maior = matriz[l][c]
            elif matriz[l][c] > maior:
                maior = matriz[l][c]

print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma de todos os números inseridos é {somapar}')
print(f'A soma dos valores da 3 coluna é {soma3c}')
print(f'O maior valor da segunda linha é {maior}')