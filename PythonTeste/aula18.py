pessoas = []
dados = []
totmai = totmen = 0

for c in range(0, 3):
    dados.append(str(input('Nome: ')).capitalize())
    dados.append(int(input('Idade: ')))
    pessoas.append(dados[:])
    dados.clear()
    print('-'*30)

for p in pessoas:
    if p[1] >= 18:
        totmai += 1
        print(f'{p[0]} é maior de idade')
        
    else:
        totmen += 1
        print(f'{p[0]} é menor de idade')

print(f'Ao todo temos {totmai} maiores de idade e {totmen} menores de idade')
