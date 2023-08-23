# Lista composta e análise de dados
pessoas = []
pesadas = []
leves = []
cont = maior_peso = menor_peso = 0
while True:
    nome = str(input('Nome:'))
    peso = float(input('Peso:'))
    pessoas.append([nome, peso])
    cont += 1
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Ss':
        continue
    elif r in 'Nn':
        break
    else:
        print('Resposta inválida')
        r = str(input('Deseja continuar? [S/N]'))
for pos, x in enumerate(pessoas):
    if pos == 0:
        maior_peso = x[1]
        menor_peso = x[1]
    else:
        if maior_peso < x[1]:
            maior_peso = x[1]
        elif x[1] < menor_peso:
            menor_peso = x[1]
for p in pessoas:
    if p[1] == maior_peso:
        pesadas.append(p[0])
    elif p[1] == menor_peso:
        leves.append(p[0])
print(f'{cont} pessoas foram cadastradas.')
print(f'O maior  peso foi {maior_peso:.2f}kg. Peso de {pesadas} ')
print(f'O menor peso foi {menor_peso:.2f}kg. Peso de {leves}')
