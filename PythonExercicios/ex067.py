while True:
    n = int(input('Queres ver a tabuada de que número? '))
    print('-'*50)

    if n < 0:
        break
    for a in range(1, 11):
        print(f'{n} x {a} = {n * a}')
    print('-'*50)

    if n < 0:
        break
print('Tabuada encerrada. Volte Sempre')
print('-=-'*20)
