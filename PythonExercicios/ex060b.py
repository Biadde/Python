# cálculo do fatorial com o FOR

print('-=-'*20)
print('Calculadora de fatoriais')
print('-=-'*20)

n = int(input('Insere um número para calcular o seu fatorial: '))
fatorial = 1

print(f'{n}! = ', end='')

for c in range(n, 0, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
 
    fatorial = fatorial * c
print(fatorial)
