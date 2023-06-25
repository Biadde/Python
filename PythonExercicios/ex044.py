print(f'\033[34m{" LOJA ":=^50}\033[m')
preço = (float(input('Preço das compras: €')))
print('''Formas de pagamento:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opção = int(input('Opção: '))

print('-'*60)

if opção == 1:
    preço_final = preço - (preço * (10 / 100))
    print(f'A tua compra de \033[1m{preço:.2f}€\033[m, no final, irá custar \033[1;33m{preço_final:.2f}€\033[m.')
elif opção == 2:
    preço_final = preço - (preço * (5 / 100))
    print(f'A tua compra de \033[1m{preço:.2f}€\033[m, no final, irá custar \033[1;33m{preço_final:.2f}€\033[m.')
elif opção == 3:
    preço_final = preço
    preço_parcela = preço_final / 2
    print(f'A tua compra de \033[1m{preço:.2f}€\033[m, será parcelada em \033[1m2\033[m parcelas de \033[1;33m{preço_parcela:.2f}€\033[m sem juros.')
    print(f'O preço final da tua compra será de \033[1;33m{preço_final:.2f}€\033[m.')
elif opção == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas <= 2:
        print('\033[1;31mNúmero de parcelas inválido.\033[m')
    else:
        preço_final = preço + (preço * (20 / 100))
        preço_parcela = preço_final / parcelas
        print(f'A tua compra de \033[1m{preço:.2f}€\033[m será parcelada em \033[1m{parcelas}\033[m parcelas de \033[1;33m{preço_parcela:.2f}€\033[m com juros.')
        print(f'O preço final da tua compra será de \033[1;33m{preço_final:.2f}€\033[m.')
else:
    print('\033[1;31mOpção de pagamento inválida. Tenta novamente!\033[m')

print('-'*60)

