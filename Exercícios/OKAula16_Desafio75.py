# Estatísticas de valores #

n = (int(input('Digite um número:')), int(input('Digite mais um número:')), int(input('Digite outro número:')), int(input('O último número:')))
print(f'Você digitou o números: {n}')
if n.count(9) != 0:
    print(f'O número 9 aparece {n.count(9)} vezes.')
else:
    print(f'O número 9 não aperece nenhuma vez.')
if 3 not in n:
    print(f'O número 3 não aparece em nenhuma posição.')
else:
    print(f'O número 3 aparace na posição de número {n.index(3) + 1}.')
pares = []
for par in n:
    if par % 2 == 0:
        pares.append(par)
if len(pares) > 0:
    print(f'Os valores pares digitados foram:{pares}')
else:
    print('Nenhum número par foi digitado.')
