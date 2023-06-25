dados = []
princ = []
cont = 0
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso[Kg]: ')))
    
    if len(princ) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    
    print('-'*45)
    princ.append(dados[:])
    dados.clear()
    cont += 1

    continuar = str(input('Queres continuar?[S/N] ')).strip().upper()

    if continuar == 'N':
        break

    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar?[S/N] ')).strip().upper()

print('-='*30)
print(f'Ao todo, foram cadastradas {cont} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in princ:
    if p[1] == maior:
        print([p[0]], end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in princ:
    if p[1] == menor:
        print([p[0]], end=' ')