lista = []
pares = []
impares = []

while True:
    n = int(input('Insere um valor:'))
    lista.append(n)
    continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    print('-'*40)

    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break
print('-=-'*25)
print(f'Inseriste os números: {lista}')
print(f'Os valores {pares} são pares')
print(f'Os valores {impares} são impares')
print('-=-'*25)