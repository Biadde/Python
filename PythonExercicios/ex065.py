continuar = 'S'
c = 0
soma = 0
maior = 0
menor = 0

while continuar == 'S':
    n = int(input('Insere um número: '))
    c += 1
    soma += n

    continuar = str(input('Queres continuar?[S/N]: ')).strip().upper()

    if continuar == 'N':
        continuar = 'N'
        print('-=-'*20)
        print('Fim do programa...')
        print('-=-'*20)

    while continuar not in 'SN':
        continuar = str(input('Opção Inválida. Tente Novamente[S/N]: ')).strip().upper()

    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

print(f'A média dos {c} números inseridos é {soma / c:.2f}')
print(f'O menor número inserido foi {menor} e o maior foi {maior}')
