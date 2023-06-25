print('\033[35m-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20, '\033[m')

reta1 = float(input('Insere o comprimento da 1ª reta: '))
reta2 = float(input('Insere o comprimento da 2ª reta: '))
reta3 = float(input('Insere o comprimento da 3ª reta: '))

print('-'*50)

# Condição para ser triângulo + Descobrir se é equilatero, escaleno ou isósceles
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    if reta1 == reta2 == reta3:
        print('É possível formar um triângulo \033[1;33mequilátero\033[m')
    elif reta1 != reta2 and reta1 != reta3 and reta2 != reta3:
        print('É possível formar um triângulo \033[1;33mescaleno\033[m')
    else:
        print('É possível formar um triângulo \033[1;33misósceles\033[m')
else:
    print('\033[1;31mNão é possível formar um triângulo com as retas acima!\033[m')

print('-'*50)

