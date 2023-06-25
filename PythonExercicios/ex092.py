from datetime import date
pessoa = {}
reformado = 0
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
pessoa['idade'] = date.today().year - int(input('Ano de nascimento: '))
pessoa['ctps'] = int(input('Carteira de trabalho [0 não tem]: '))
if pessoa['ctps'] != 0:
    pessoa['anos de serviço'] = date.today().year - int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: €'))
else:
    pessoa['anos de serviço'] = 0
print('-='*30)
for k,v in pessoa.items():
    print(f'   - {k} tem o valor {v}')

if pessoa['anos de serviço'] >= 35:
    print(f'{pessoa["nome"]} já tem anos de serviço suficientes para se aposentar')

elif pessoa['anos de serviço'] == 0:
    print(f'{pessoa["nome"]} precisa começar a trabalhar antes de se aposentar!')
else:
    aposentadoria = (35 - pessoa['anos de serviço']) + pessoa['idade']
    print(f'{pessoa["nome"]} poderá se aposentar com {aposentadoria} anos')
print('-='*30)
