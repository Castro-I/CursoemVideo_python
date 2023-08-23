#Jogo de dadods em python
from random import randint
from operator import itemgetter
resultados = {'jogador 1': randint(1, 6),
              'jogador 2': randint(1, 6),
              'jogador 3': randint(1, 6),
              'jogador 4': randint(1, 6)}
print(F'{"VALORES SORTEADOS:":^24}')
for k, v in resultados.items():
    print(f'{k} caiu {v}')
print('=-' * 12)
ranking = sorted(resultados.items(), key=itemgetter(1), reverse=True)
print(f'{"RANKING:":^24}')
for k, v in enumerate(ranking):
    print(f'{k + 1}o lugar: {v[0]} com {v[1]}')
