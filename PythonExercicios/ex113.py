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


def leiaFloat(a):
    while True:
        try:
            n = float(input(a))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: Por favor, insere um número real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[1;31mO usuário preferiu não inserir este número.\033[m')
            return 0
        else:
            break
    return n


int = leiaInt('Insere um Inteiro: ')
real = leiaFloat('Insere um Real: ')
print(f'O valor inteiro inserido foi {int} e o real foi {real}')
