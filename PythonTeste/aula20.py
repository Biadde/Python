def contador(* num):
    tam = len(num)
    print(f'Ao todo, recebi {tam} números:')
    for valor in num:
        print(f'{valor} ', end='')
    print('Fim!')


contador(1, 4, 5, 8, 3)
contador(0, 2)
contador(4, 6, 3, 2)