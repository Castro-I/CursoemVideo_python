#Dicionário em Python
Aluno = dict()
Aluno['nome'] = str(input('Nome do aluno:'))
Aluno['média'] = float(input(f'Média de {Aluno["nome"]}:'))
if Aluno['média'] < 6.0:
    Aluno['situação'] = 'Reprovado(a)'
else:
    Aluno['situação'] = 'Aprovado(a)'
for k, v in Aluno.items():
    print(f'{k} do(a) aluno(a) = {v}')
    