lista = []
cont = 0
soma_idd = 0
lista_mulheres = []
idd_elevada = []

while True:
    pessoas = {}
    pessoas['nome'] = str(input('Nome: ')).strip().capitalize()
    pessoas['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    while 'M' not in pessoas['sexo'] and 'F' not in pessoas['sexo']:
        pessoas['sexo'] = str(input('Sexo[M/F]: ')).strip().upper()
    if pessoas['sexo'] == 'F':
        lista_mulheres.append(pessoas['nome'])
    pessoas['idade'] = int(input('Idade: '))
    lista.append(pessoas.copy())
    cont += 1
    soma_idd += pessoas['idade']
    print('-='*30)
    continuar = str(input('Queres continuar[S/N]? ')).strip().upper()
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar[S/N]? ')).strip().upper()
    if continuar == 'N':
        break
    print('-='*30)

media = soma_idd / cont

for pessoa in lista:
    if pessoa['idade'] > media:
        idd_elevada.append(pessoa['nome'])
print('-='*30)
print(f'   - Foram cadastradas {cont} pessoas')
print(f'   - A média da idade do grupo é de {media:.2f} anos')
print(f'   - As mulheres cadastradas foram {lista_mulheres}')
print(f'   - As pessoas com idade acima da média são {idd_elevada}')
print('-='*30)
