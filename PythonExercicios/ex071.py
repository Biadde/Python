print('='*40)
print(f'{"BANCO":^40}')
print('='*40)

valor = int(input('Quanto dinheiro queres levantar? €'))
total = valor
nota = 500
totnota = 0

while True:
    if total >= nota:
        total -= nota
        totnota += 1
    else:
        if totnota > 0:
            print(f'Total de {totnota} notas de {nota}€')
        if nota == 500:
            nota = 200
        elif nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totnota = 0
        if total == 0:
            break
print('=' * 40)
print('Volte sempre! Tenha um bom dia!')