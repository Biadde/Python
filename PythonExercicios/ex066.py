cont = 0
soma = 0

while True:
    n = int(input('Insere um número [999 para parar]: '))
    if n == 999:
        break
    cont += 1
    soma += n
print('-=-'*20)
print(f'Ao todo foram inseridos {cont} números e a sua soma é {soma}')
print('-=-'*20)
