
from time import sleep

print('-=-'*15)
print('Contagem regressiva')
print('-=-'*15)

for c in range(10, -1, -1):
    sleep(1)
    print(c)