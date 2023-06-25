
print('-'*70)
frase = input('Escreve uma frase: ').strip().lower()
quantidade = frase.count('a') + frase.count('á') + frase.count('à') + frase.count('ã') + frase.count('â')
primeiro_a = frase.find('a') + 1
ultimo_a = frase.rfind('a') + 1

                    
print(f'Na frase "{frase.capitalize()}", a letra "A" aparece: {quantidade} vezes')

print(f'O primeiro "A" encontrado na frase "{frase.capitalize()}" está na posição: {primeiro_a}')
print(f'O último "A" encontrado na frase "{frase.capitalize()}" está na posição: {ultimo_a}')
print('-'*70)
