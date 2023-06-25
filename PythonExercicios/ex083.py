expressao = str(input('Insere a expressão: '))
pilha = []

for simb in expressao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Esta expressão é válida!')
else:
     print('Esta expressão está errada!')
print('-=-'*25)