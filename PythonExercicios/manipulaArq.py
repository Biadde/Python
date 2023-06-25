# Manipulação de arquivos

# w (write): Abre um arquivo no modo escrita mas substitui o conteudo que já existe no arquivo
# a (append): Também modo escrita, mas mantém
# r (read): Abre o arquivo no modo leitura

arquivo = open('pessoas.txt', 'a+')
arquivo.write('Linha\n')

arquivo.close()
