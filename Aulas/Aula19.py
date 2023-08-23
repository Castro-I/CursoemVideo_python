#Dicionários'{}'
pessoas = {'nome': 'José', 'idade': '34', 'sexo': 'Masculino', 'peso': '78'}
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
print(pessoas)
print(pessoas['nome'])
print(pessoas['idade'])
print(pessoas['sexo'])
print(pessoas['peso'])
del pessoas['peso']
print(pessoas)
pessoas['nome'] = 'André'
pessoas['idade'] = 27
print(pessoas)

for k, v in pessoas.items():
    print(f'{k} = {v}.')

Brasil = list()
estado1 = {'UF': 'Distrito federal', 'Sigla': 'DF'}
estado2 = {'UF': 'São Paulo', 'Sigla': 'SP'}
Brasil.append(estado1)
Brasil.append(estado2)
estado = dict()
for c in range(0, 2):
    estado['UF'] = str(input('Nome do estado:'))
    estado['Sigla'] = str(input('Sigla:'))
    Brasil.append(estado.copy())
for e in Brasil:
    for k, v in e.items():
        print(f'{k}: {v}', end=' ')
        print('')


