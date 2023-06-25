numeros = []
for cont in range(0, 5):
    n = int(input('Insere um valor: '))
    if cont == 0:           # se for o primeiro número
        numeros.append(n)
    elif n > numeros[-1]:   # se for maior que o ultimo
        numeros.append(n)
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                break
            pos += 1

print('-=-'*30)
print(f'Os valores inseridos em ordem são: {numeros}')