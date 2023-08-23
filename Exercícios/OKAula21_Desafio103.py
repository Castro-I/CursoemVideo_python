# ficha
def ficha(n='<desconhecido>', g='0'):
    return print(f'O jogador {n} marcou {g} gol(s) na temporadas.')


#Programa principal
nome = str(input('Nome do jogador:'))
gols = str(input('Quantidade de gols:'))
if nome and gols != '':
    ficha(n=nome, g=gols)
elif nome == gols == '':
    ficha()
elif nome != '' and gols == '':
    ficha(n=nome)
elif nome == '' and gols != '':
    ficha(g=gols)
