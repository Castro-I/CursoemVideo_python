#Aprimorando os Dicionários

BD = list()
jogador = dict()
while True:
    jogador['nome'] = str(input('Nome do jogador:'))
    jogador['partidas'] = int(input('Partidas jogadas:'))
    jogador['gols'] = list()
    for pos, g in enumerate(range(0, jogador['partidas'])):
        gols = jogador['gols'].append(int(input(f'Gols marcados na partida {pos + 1}:')))
    jogador['total de gols'] = sum(jogador['gols'])
    BD.append(jogador.copy())
    print('__' * 12)
    r = str(input('Deseja continuar? [S/N]')).upper()
    while r not in 'NS':
        print('Rsposta inválida.')
        r = str(input('Deseja continuar? [S/N]')).upper()
    if r in 'Nn':
        break
print('__' * 12)
nJ = 0
while nJ != 999:
    nJ = int(input(f'Qual jogador deseja consultar? (1 ao {len(BD)})'))
    if nJ == 999:
        break
    elif nJ > len(BD):
        print('Jogador não cadastrado.')
        print('__' * 12)
        continue
    for k, v in BD[nJ - 1].items():
        print(f'{k} = {v}')
    print('__' * 12)
print('..... VOLTE SEMPRE .....')
