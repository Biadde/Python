from datetime import date
print('-'*50)
ano = int(input('Insere um ano: '))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:  # Descobrir se o ano é bissexto
    # Descobrir o tempo verbal da frase
    if ano == date.today().year:
        print(f'O ano {ano} \033[1;32mé bissexto\033[m')
    if ano > date.today().year:
        print(f'O ano {ano} \033[1;32mserá bissexto\033[m')
    if ano < date.today().year:
        print(f'O ano {ano} \033[1;32mfoi bissexto\033[m')
else:
    if ano == date.today().year:
        print(f'O ano {ano} \033[1;31mnão é bissexto\033[m')
    if ano > date.today().year:
        print(f'O ano {ano} \033[1;31mnão será bissexto\033[m')
    if ano < date.today().year:
        print(f'O ano {ano} \033[1;31mnão foi bissexto\033[m')
print('-'*50)
