def aumentar(preço=0, perc=0, formato=False):
    '''param preço: Preço
    param perc: Percentagem que deseja adicionar ao número
    param formato: [Opcional] Formata os preços
    return: Retorna o valor do número com o aumento
    '''
    aumento = preço + (perc * preço / 100)
    return aumento if formato is False else moeda(aumento)


def diminuir(preço=0, perc=0, formato=False):
    '''param preço: Preço
    param perc: Percentagem que deseja retirar do número
    param formato: [Opcional] Formata os preços
    return: Retorna o valor do número com o desconto
    '''
    dim = preço - (perc * preço / 100)
    return dim if formato is False else moeda(dim)


def dobro(preço=0, formato=False):
    '''param preço: Preço
    param formato: [Opcional] Formata os preços
    return: Retorna o dobro do número
    '''
    dobro = preço * 2
    return dobro if formato is False else moeda(dobro)


def metade(preço=0, formato=False):
    '''param preço: Preço
    param formato: [Opcional] Formata os preços
    return: Retorna a metade do número'''
    metade = preço / 2
    return metade if formato is False else moeda(metade)


def moeda(preço=0, moeda='€'):
    return f'{preço:.2f}{moeda}'.replace('.', ',')
