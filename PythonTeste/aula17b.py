valores = []
for cont in range(0, 5):
    valores.append(int(input('Insere um valor: ')))
    print('-'*30)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}!')
print('Cheguei ao final da lista.')