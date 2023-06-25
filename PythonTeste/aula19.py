estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: ')).title().strip()
    estado['sigla'] = str(input('Sigla do Estado: ')).strip().upper()
    brasil.append(estado.copy())
    print('-='*30)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
