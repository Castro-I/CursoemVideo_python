#Cadastro de jogador de futebol

aproveitamento = dict()
aproveitamento['nome'] = str(input('Nome do jogador:'))
aproveitamento['partidas'] = int(input(f'Quantas partidas {aproveitamento["nome"]} jogou?'))
aproveitamento['gols'] = list()
for num, p in enumerate(range(0, aproveitamento['partidas'])):
    gols = aproveitamento['gols'].append(int(input(f'Gols marcados na partida {num + 1}:')))
aproveitamento['total'] = sum(aproveitamento['gols'])
print('_' * 50)
print(f'O jogador {aproveitamento["nome"]} jogou {aproveitamento["partidas"]} partidas:')
for part, g in enumerate(aproveitamento['gols']):
    print(f'=>', f'Na partida {part + 1}, {aproveitamento["nome"]} marcou {g} gols.')
print(f'Total de gols: {aproveitamento["total"]}')
