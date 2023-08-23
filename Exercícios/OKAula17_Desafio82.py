# Dividindo valores em lista

l1 = []
par = []
impar = []
while True:
    l1.append(int(input('Digite um valor:')))
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if r in 'S':
        continue
    elif r in 'N':
        break
    else:
        r = str(input('Resposta inválida.\nDeseja continuar? [S/N]')).strip().upper()[0]
for x in l1:
    if x % 2 == 0:
        par.append(x)
    else:
        impar.append(x)
print(f'A lista ficou assim: {sorted(l1)}\nOs números pares são: {par}\nOs ímpares são: {impar}')
