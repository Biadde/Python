def ajuda():
    from time import sleep
    while True:
        print('\033[43m~'*25)
        print('    SISTEMA DE AJUDA  ')
        print('~'*25, '\033[m')
        biblioteca = str(input('Função ou biblioteca > ')).lower()
        if biblioteca == 'fim':
            break
        print('\033[45m~'*42)
        print(f'  A acessar o manual do comando "{biblioteca}"...  ')
        print('~'*42, '\033[m')
        sleep(1)
        print(f'{help(biblioteca)}')
    print('\033[41m~'*17)
    print('  VOLTE SEMPRE!  ')
    print('~'*17, '\033[m')
print(ajuda())