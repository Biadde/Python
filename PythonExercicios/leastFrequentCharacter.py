def count_letters(msg):
    dic = {}
    frase = msg.strip().upper()
    for palavra in frase.split():
        for letra in palavra:
            if letra in dic:
                dic[letra] += 1
            else:
                dic[letra] = 1
    ordenado = sorted(dic.items(), key=lambda item: item[1])
    dic = dict(ordenado)
    print(f'A letra {list(dic.keys())[0]} foi encontrada {list(dic.values())[0]} vez(es)')


count_letters('Apita o comboio')

