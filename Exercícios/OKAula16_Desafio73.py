# Tabela Brasileirão #
def print_lines():
    print('='*50)


Brasileirao = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR',
               'Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
               'Cuiabá', 'Ceará SC', 'Atlético-GO', 'Avaí', 'Juventude')
print('Os cinco primeiros colocados são:')
print_lines()
for x in Brasileirao[0:5]:
    print(x)
print_lines()
print('Os quatro últimos colocados são:')
print_lines()
for y in Brasileirao[-4:]:
    print(y)
print_lines()
print(F'Os time em ordem alfabética:\n{sorted(Brasileirao)}')
print_lines()
print('Coritiba se encontra na posição de número:{}'.format(Brasileirao.index('Coritiba') + 1))
