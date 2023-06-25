numeros = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
    'treze', 'catorze', 'quinze', 'dezasseis', 'dezassete', 'dezoito', 'dezanove', 'vinte')

print('-=-'*20)
n = int(input('Insere um número de 0 a 20: '))
print('-=-'*20)

while n < 0 or n > 20:
    print('\033[1;31mResposta Inválida. Tenta Novamente!\033[m')
    n = int(input('Insere um número de 0 a 20: '))

print(f'Inseriste o número \033[1;33m{numeros[n]}\033[m')