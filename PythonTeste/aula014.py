n = 1
par = 0
impar = 0

while n != 0:
    n = int(input('Insere um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        elif n % 2 == 1:
            impar += 1

print('-'*45)
print(f'Foram inseridos {par} números pares e {impar} números ímpares')
