print('-=-'*20)
numeros = (int(input('Insere o 1º valor: ')), int(input('Insere o 2º valor: ')), int(input('Insere o 3º valor: ')),
            (int(input('Insere o 4º valor: '))))
print('-=-'*20)        

print(f'Tu inseriste os números {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi inserido em nenhuma posição ')

print(f'Os valores pares inseridos foram:', end=' ')

for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')


print('\n','-=-'*20)