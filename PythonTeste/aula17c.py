a = [2, 3, 4, 7]
b = a[:]    # B receber todos os itens de A, sem criar uma ligação
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')