print('-=-'*20)
print(f'{"LOJA DA ROUBALHEIRA":^55}')
print('-=-'*20)

cont = 0
total = 0
prod_caros = 0
menor = 0
barato = ''

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: €'))
    print('-'*45)

    cont += 1
    total += preco
    if preco > 1000:
        prod_caros += 1

    if cont == 1 or preco < menor:
        menor = preco
        barato = nome

    continuar = str(input('Queres continuar?[S/N]: ')).strip().upper()[0]
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Resposta Inválida. Tente Novamente: ')).strip().upper()[0]

    if continuar == 'N':
        break
print(f'{" FIM DO PROGRAMA ":-^40}')
print(f'O total da compra foi {total:.2f}€')
print(f'Ao todo, temos {prod_caros} produtos a custar mais de 1000.00€')
print(f'O produto mais barato foi {barato.capitalize()} que custa {menor:.2f}€')