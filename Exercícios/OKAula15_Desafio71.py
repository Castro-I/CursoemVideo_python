#Simulador de Caixa Eletrônico#

valor = int(input('Qual valor deseja sacar?'))
cinquenta = vinte = dez = um = 0
while True:
    if valor // 50:
        cinquenta += 1
        valor -= 50
    else:
        break
while True:
    if valor // 20:
        vinte += 1
        valor -= 20
    else:
        break
while True:
    if valor // 10:
        dez += 1
        valor -= 10
    else:
        break
while True:
    if valor // 1:
        um += 1
        valor -= 1
    else:
        break

if cinquenta != 0:
    print(f'Total de {cinquenta} cédulas de R$ 50,00.')
if vinte != 0:
    print(f'Total de {vinte} cédulas de R$ 20,00.')
if dez != 0:
    print(f'Total de {dez} cédulas de R$ 10,00.')
if um != 0:
    print(f'Total de {um} cédulas de R$ 1,00.')
