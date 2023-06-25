def dobro(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

        
lista = [9, 5, 3, 2, 5, 7]
dobro(lista)
print(lista)