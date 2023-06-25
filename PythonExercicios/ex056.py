somaidd = 0
mediaidd = 0
maioriddhomem = 0
nomevelho = ''
totmulher20 = 0


for a in range(1, 5):
    print(f'------ {a}ª PESSOA ------')
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidd = somaidd + idade

    if a == 1 and sexo == 'M':
        maioriddhomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioriddhomem:
        maioriddhomem = idade
        nomevelho = nome

    if sexo == 'F' and idade < 20:
        totmulher20 = totmulher20 + 1

print('-'*45)
mediaidd = somaidd / 4
print(f'A média de idade do grupo é de {mediaidd} anos.')
print(f'O homem mais velho é o {nomevelho} e tem {maioriddhomem} anos.')
print(f'Ao todo são {totmulher20} mulher(es) com menos de 20 anos.')
