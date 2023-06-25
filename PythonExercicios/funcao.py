def primo(n):
    divisores = 0
    for cont in range(1, n+1):
        if n % cont == 0:
            divisores += 1

    if divisores == 2:
        return True
    else:
        return False
    

num = int(input('Insere um número: '))
print(primo(num))
