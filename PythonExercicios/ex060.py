# cálculo do fatorial com o WHILE

print('-=-'*20)
print('Calculadora de fatoriais')
print('-=-'*20)

n = int(input('Insere um número para calcular o seu fatorial: '))
c = n
fatorial = 1
print(f'{n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial = fatorial * c
    c = c - 1

print(fatorial)
