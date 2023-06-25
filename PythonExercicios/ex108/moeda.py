def aumentar(preço=0, perc=0):
    '''param preço: Preço
    param perc: Percentagem que deseja adicionar ao número
    return: Retorna o valor do número com o aumento
    '''
    aumento = preço + (perc * preço / 100)
    return aumento


def diminuir(preço=0, perc=0):
    '''param preço: Preço
    param perc: Percentagem que deseja retirar do número
    return: Retorna o valor do número com o desconto
    '''
    dim = preço - (perc * preço / 100)
    return dim


def dobro(preço=0):
    '''param preço: Preço
    return: Retorna o dobro do número
    '''
    dobro = preço * 2
    return dobro


def metade(preço=0):
    '''param preço: Preço
    return: Retorna a metade do número'''
    metade = preço / 2
    return metade


def moeda(preço=0, moeda='€'):
    return f'{preço:.2f}{moeda}'.replace('.', ',')
