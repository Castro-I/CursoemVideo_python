#Tabuada#

print('Vamos fazer algumas tabuadas:')
print('-' * 30)
while True:
    n = int(input('Digite o valor:'))
    if n < 0:
        break
    t = 1
    for x in range(0, 10):
        print(f'{t} x {n} = {t*n}')
        t += 1
    print('-' * 30)

print('Fim.')
