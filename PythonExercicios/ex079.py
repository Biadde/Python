numeros = []

while True:
    n = int(input('Insere um valor: '))
    if n in numeros:
        print('\033[31mValor duplicado! Não será adicionado\033[m')
    else:
        numeros.append(n)
        print('\033[32mValor adicionado com sucesso...\033[m')

    continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    print('-'*45)

print('-=-'*25)
print(f'Inseriste os valores: {sorted(numeros)}')
print('-=-'*25)