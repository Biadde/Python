num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não encontrei o número 4')
print(num)
print(f'Esta lista tem {len(num)} elementos')