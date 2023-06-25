def leiaInt(a):
    while True:
        try:
            n = int(input(a))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, insere um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não inserir este número.\033[m')
            return 0
        else:
            break
    return n


def linha(tam=42):
    print('-'*tam)


def cabecalho(txt):
    linha()
    print(txt.center(42))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c+=1
    linha()
    opc = leiaInt('\033[32mSua Opção:\033[m ')
    return opc

