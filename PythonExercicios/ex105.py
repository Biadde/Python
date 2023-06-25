def notas(*n, sit=False):
    '''--> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma
    '''

    notas = {}
    notas['total'] = len(n)
    notas['maior'] = max(n)
    notas['menor'] = min(n)
    notas['média'] = (sum(n) / notas['total'])
    if sit:
        if notas['média'] < 50:
            notas['situacao'] = 'NEGATIVA'
        elif notas['média'] >= 50 and notas['média'] < 70:
            notas['situacao'] = 'RAZOÁVEL'
        elif notas['média'] >= 70:
            notas['situacao'] = 'BOA'

    return notas


lista = []
while True:
    lista.append(float(input('Nota: ')))
    continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    while 'S' not in continuar and 'N' not in continuar:
        print('\033[31mResposta Inválida! Tente novamente.\033[m')
        continuar = str(input('Queres continuar?[S/N] ')).strip().upper()
    if continuar == 'N':
        break

print(notas(*lista, sit=True))