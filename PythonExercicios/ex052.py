print('-=-'*15)
print('Números primos')
print('-=-'*15)

numero = int(input('Insere um número: '))
total = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=" ")
        total = total + 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print('\033[m')
print(f'O número {numero} foi divisivel {total} vezes')
if total == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
