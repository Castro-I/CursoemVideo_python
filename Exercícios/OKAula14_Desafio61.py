# Lendo os valores
p1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
n = 2
cont = 0
# Montando a PA
PA = [p1, ]
while cont != 9:
    Pn = p1 + (n - 1) * r
    n += 1
    cont += 1
    PA.append(Pn)
print('PA = {}'.format(PA))
