from math import pow, sqrt

print('-'*50)
cateto1 = float(input('Insere o valor de um cateto em Cm: '))
cateto2 = float(input('Insere o valor do outro cateto em Cm: '))
hipotenusa_quadrado = pow(cateto1, 2) + pow(cateto2, 2)



print(f'A hipotenusa deste triângulo retângulo é de: {sqrt(hipotenusa_quadrado):.2f} Cm ')
print('-'*50)