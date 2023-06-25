print('-'*50)
cidade = input('Insere o nome de uma cidade: ').strip().title()
cidade_santo = 'Santo' in cidade

if cidade_santo == True:
    localizacao = cidade.find('Santo')

    if localizacao == 0:
        print(f'Sim, {cidade} começa com a palavra "Santo"')
    else:
        print(f'Não, {cidade} não começa com a palavra "Santo"')

else:
    print(f'{cidade} não tem a palavra "Santo"')
print('-'*50)