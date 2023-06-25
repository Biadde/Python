print('\033[35m-=-'*20)
print('Analisador de Triângulos')
print('-=-'*20,'\033[m')
reta1 = float(input('Insere o comprimento da \033[33m1ª\033[m reta: '))
reta2 = float(input('Insere o comprimeto da \033[33m2ª\033[m reta: '))
reta3 = float(input('Insere o comprimento da \033[33m3ª\033[m reta: '))


# Condição para ser um triângulo
if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta1 + reta2:
    print('\033[32mÉ possível formar um triângulo com as retas acima\033[m')
else:
    print('\033[31mNão é possível formar um triângulo com as retas acima\033[m')
print('-'*70)