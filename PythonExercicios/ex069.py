total = 0
c_18 = 0
c_homem = 0
c_mulher_20 = 0

while True:
    print('-'*35)
    print('       Cadastra uma pessoa   ')
    print('-'*35)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).strip().upper()
    total += 1

    if idade > 18:
        c_18 += 1

    if sexo == 'M':
        c_homem += 1

    if sexo == 'F' and idade < 20:
        c_mulher_20 += 1

    while 'M' not in sexo and 'F' not in sexo:
        sexo = str(input('Resposta Inválida. Tente Novamente: ')).strip().upper()

    print('-'*35)
    continuar = str(input('Quer continuar?[S/N]: ')).strip().upper()
    while 'S' not in continuar and 'N' not in continuar:
        continuar = str(input('Resposta Inválida. Tente Novamente: ')).strip().upper()

    if continuar == 'N':
        break

print('========== FIM DO PROGRAMA ===========')
print(f'Total de pessoas com mais de 18 anos: \033[1;33m{c_18}\033[m')
print(f'Ao todo temos \033[1;33m{c_homem}\033[m homens cadastrados')
print(f'E temos \033[1;33m{c_mulher_20}\033[m mulheres com menos de 20 anos')
print('-=-'*20)
