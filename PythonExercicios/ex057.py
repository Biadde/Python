print('-'*45)
sexo = str(input('Insere o teu sexo[M/F]: ')).strip().upper()

while sexo != 'F' and sexo != 'M':
    sexo = str(input('Dados Inválidos. Por favor, informe o seu sexo: ')).strip().upper()
print('-'*45)
print(f'Sexo {sexo} registrado com sucesso')
