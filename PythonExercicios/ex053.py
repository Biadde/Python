print('-=-'*15)
print('Detector de Palíndromo')
print('-=-'*15)

frase = str(input('Escreve uma frase: ')).strip().upper()

print('-'*45)

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(f'O inverso de \033[1m{junto}\033[m é \033[1;33m{inverso}\033[m')
if inverso == junto:
    print('A frase inserida \033[1;32mé\033[m um \033[1mpalíndromo!\033[m')
else:
    print('A frase inserida \033[1;31mnão\033[m é um \033[1mpalíndromo!\033[m')
