#COntinuação Desafio 61

'''Lendo valores'''

p1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
n = 1
PA = []
for x in range(0, 10):
    x = p1 + (n - 1) * r
    n += 1
    PA.append(x)
print('PA = {}'.format(PA))

'''Montando loop'''

p1 = (x + r)
n = 1
PA2 = []
res = int(input('Deseja vizualizar quantos termos?'))
while res != 0:
    for y in range(0, res):
        y = p1 + (n - 1) * r
        n += 1
        PA2.append(y)
    print('PA = {}'.format(PA2))
    res = int(input('Deseja vizualizar quantos termos?'))
    if res == 0:
        print('FIM.')
