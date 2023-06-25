from time import sleep
lista = []


def maior(lst):
    maior = max(lista)
    print('A analisar os valores...')
    sleep(1)
    print(f'Ao todo foram inseridos {len(lista)} valores')
    print(f'O maior valor inserido foi {maior}')


while True:
    lista.append(int(input('Insere um valor: ')))
    print('-='*30)
    continuar = str(input('Queres continuar[S/N]? ')).strip().upper()
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Queres continuar[S/N]? ')).strip().upper()
    if continuar == 'N':
        break
    print('-='*30)
print('-='*30)
maior(lista)