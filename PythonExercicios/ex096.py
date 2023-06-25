def area(a, b):
    area = a * b
    print('-'*50)
    print(f'A área de um terreno de {a} x {b} é de {area:.2f}m².')

print('-='*15)
print('     Controle de Terrenos    ')
print('-='*15)
area(float(input('Largura(m): ')), (float(input('Comprimento(m): '))))