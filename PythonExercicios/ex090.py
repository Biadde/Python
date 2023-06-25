notas = {}

notas['nome'] = (str(input('Nome: '))).strip().capitalize()
notas['media'] = (float(input(f'Média de {notas["nome"]}: ')))

if notas['media'] >= 50:
    notas['situacao'] = 'APROVADO'
else:
    notas['situacao'] = 'REPROVADO'
print(f'{notas["nome"]} teve uma média de {notas["media"]:.2f}% e foi {notas["situacao"]}')