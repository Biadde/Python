def parOuImpar(a):
    if a % 2 == 0:
        return True
    else:
        return False
    

n = int(input('Insere um número: '))
if parOuImpar(n) == True:
    print(f'O número {n} é par')
elif parOuImpar(n) == False:
    print(f'O número {n} é ímpar')