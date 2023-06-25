lista = []
for a in range(1, 6):
    lista.append(int(input('Insere um valor: ')))

maior = max(lista)
menor = min(lista)
print('-=-'*20)
print(f'Tu inseriste os valores: {lista}')
print(f'O maior número inserido foi {maior}')
print(f'O menor número inserido foi: {menor}')
print('-=-'*20)

