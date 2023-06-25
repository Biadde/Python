print('-=-'*20)
equipas = ('SL Benfica', 'FC Porto', 'SC Braga', 'Sporting CP', 'FC Arouca', 'Vitória SC', 'FC Famalicão', 'GD Chaves',
           'FC Vizela', 'Casa Pia AC', 'Rio Ave FC', 'Boavista FC', 'Portimonense', 'Gil Vicente FC',
           'Estoril Praia', 'Marítimo M.', 'FC P.Ferreira', 'Santa Clara')

print(f'Lista de equipas da Primeira Liga: {equipas}')
print('-=-'*20)
print(f'Os primeiros 5 colocados são: {equipas[:5]}')
print('-=-'*20)
print(f'Os últimos 4 colocados são: {equipas[-4:]}')
print('-=-'*20)
print(f'Equipas em ordem alfabética: {sorted(equipas)}')
print('-=-'*20)
print(f'O Portimonense está na {equipas.index("Portimonense")+ 1}ª posição')