def voto(a):
    from datetime import date
    idd = date.today().year - a
    if idd < 18:
        voto = f'Com {idd} anos: NÃO VOTA'
    elif idd >= 18 and idd < 65:
        voto = f'Com {idd} anos: VOTO OBRIGATÓRIO'
    else:
        voto = f'Com {idd} anos: VOTO OPCIONAL'
    return voto


print('-='*30)
nasc = int(input('Insere a tua data de nascimento: '))
print(voto(nasc))
print('-='*30)