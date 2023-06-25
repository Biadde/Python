print('-=-'*15)
print('Maior e menor da sequência')
print('-=-'*15)

lista = []

for a in range(1, 6):
    peso = float(input(f'Insere o peso da {a}ª pessoa: '))
    print('-'*45)
    lista.append(peso)
lista_ordenada = sorted(lista)

menor = lista_ordenada[0]
maior = lista_ordenada[4]

print(f'''O menor peso inserido foi \033[1;33m{menor:.2f} Kg\033[m
O maior peso inserido foi \033[1;33m{maior:.2f} Kg\033[m''')
