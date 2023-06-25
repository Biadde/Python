# Ler um arquivo

# Usamos o r para ler
arquivo = open('pessoas.txt', 'r')
lista = arquivo.readlines()
for linha in lista:
    print(linha.strip())

arquivo.close()
