def soma(*num):
    s = 0
    for v in num:
        s += v
    print(f'Somando os valores {num} temos {s}')


soma(2, 4)
soma(2, 8, 9)