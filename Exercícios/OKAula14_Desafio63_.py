# Sequência de Fibonacci
''' Lendo os valores'''

n = int(input('Digite um número inteiro:'))
f1 = f2 = 1
f3 = f1 + f2
cont = 4
fb = [0, f1, f2, f3]

''' Montando programa'''

if n == 0:
    print('Fim')
elif n == 1:
    print('Sequeência de Fibonacci vazia.')
elif n == 2:
    print('Sequência de Fibonacci com 2 termos:\n[0, 1]')
elif n == 3:
    print('Sequência de fibonacci com 3 termos:\n[0, 1, 1]')
else:
    while cont != n:
        Fn = (fb[-1]) + (fb[-2])
        fb.append(Fn)
        cont += 1
    print('Sequência de Fibonacci com {} termos\n{}'.format(n, fb))
print('Fim.')
