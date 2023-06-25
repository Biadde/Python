
print('-'*50) #Fazer linha horizontal
n1 = int(input('Insere um valor: '))
print('-'*50) #Fazer linha horizontal
n2 = int(input('Insere outro valor: '))

s = n1 + n2
sb = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 //n2
p = n1 ** n2
rd = n1 % n2

print('-'*50) #Fazer linha horizontal

print(f'A soma de {n1} e {n2} vale {s}')
print(f'A subtração de {n1} e {n2} vale {sb}')
print(f'A multiplicação de {n1} por {n2} vale {m}')
print(f'A divisão de {n1} por {n2} vale {d:.3f}')
print(f'A divisão inteira de {n1} por {n2} vale {di}')
print(f'{n1} elevado a {n2} vale {p}')
print(f'O resto da divisão de {n1} por {n2} vale {rd}')



