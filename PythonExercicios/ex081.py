numeros = []
cont = 0
print('-=-'*25)
while True:
    n = numeros.append(int(input('Insere um valor: ')))
    cont += 1
    continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break
    else:
        while 'S' not in continuar and 'N' not in continuar:
            continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    print('-'*40)
print('-=-'*25)
print(f'Ao todo foram inseridos {cont} valores')
print(f'Os valores em ordem decrescente são: {sorted(numeros, reverse=True)}')
if 5 in numeros:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
print('-=-'*25)