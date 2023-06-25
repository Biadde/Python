from utilidades import moeda

def leiaDinheiro(msg):
    valido = False
    while not valido:
            entrada = str(input(msg)).replace(',', '.').strip()
            if entrada.isalpha() or entrada == '':
                print(f'\033[1;31mERRO: "{entrada}" é um preço inválido!\033[m')
            else:
                valido = True
                return float(entrada)
           
def leiaInt(a):
    while True:
        n = str(input(a))
        if not n.isnumeric():
            print('\033[31mERRO! Insere um número inteiro válido.\033[m')
        else:
            valor = int(n)
            break
    return valor