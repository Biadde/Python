from time import sleep


def contador(inicio, fim, passo):
    print('-='*20)
    if passo < 0:
        passo = abs(passo)
    if passo == 0:
        passo = 1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(2)

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += passo
        print()
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ',end='', flush=True)
            sleep(0.5)
            cont -= passo
        print()


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é a tua vez de personalizar a contagem!')
sleep(1)
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))
contador(ini, fim, pas)