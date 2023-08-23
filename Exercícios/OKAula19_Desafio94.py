# Unindo dicionários e listas
grupo = list()
individuo = dict()
T_idades = 0
while True:
    individuo['nome'] = str(input('Nome: '))
    individuo['sexo'] = str(input('Sexo[M/F]: ')).upper()
    while individuo['sexo'] not in 'MF':
        individuo['sexo'] = str(input('Digite apenas M ou F.\nSexo[M/F]: ')).upper()
    individuo['idade'] = int(input('Idade: '))
    T_idades += individuo['idade']
    grupo.append(individuo.copy())
    r = str(input('Deseja continuar? [S/N]')).upper()
    if r in 'N':
        break
    else:
        while r not in 'NS':
            r = str(input('Digite apenas S ou N.\nDeseja continuar? [S/N]')).upper()
        if r in 'N':
            break
print('-=' * 12)
print(f'Total de pessoas cadastradas: {len(grupo)}')
print(f'Média de idade do grupo: {T_idades / len(grupo):.1f}')
mulheres = list()
M_idade = list()
for pos, m in enumerate(grupo):
    if m['sexo'] == 'F':
        mulheres.append(m['nome'])
    if m['idade'] > (T_idades / len(grupo)):
        M_idade.append(m)
print(f'Mulheres cadastradas: {mulheres}')
print(f'Pessoas acima da média etária:')
for k, v in enumerate(M_idade):
    print(f'nome= {v["nome"]}; sexo = {v["sexo"]}; idade = {v["idade"]}')
print('<<< ENCERADO >>>')
