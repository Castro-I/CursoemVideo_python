#Cadastro de trabalhador em Python
from datetime import datetime
trabalhador = dict()
trabalhador['Nome'] = str(input('Nome:'))
anoN = int(input('Ano de nascimento:'))
trabalhador['Idade'] = datetime.now().year - anoN
trabalhador['CTPS'] = int(input('Número da Carteira de trabalho["0" caso não tenha]:'))
if trabalhador['CTPS'] != 0:
    trabalhador['Ano de contratação'] = int(input('Ano de contratação:'))
    trabalhador['Salário'] = float(input('Salário:'))
    trabalhador['Idade  para aposentar-se'] = trabalhador['Idade'] + 35
print('-=' * 36)
for k, v in trabalhador.items():
    print(f'{k}: {v}')
