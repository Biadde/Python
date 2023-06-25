lista = []

while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append([[nome], [nota1, nota2], [media]])


    continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
print('-='*30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0][0]:<10}{a[2][0]:>8.1f}')