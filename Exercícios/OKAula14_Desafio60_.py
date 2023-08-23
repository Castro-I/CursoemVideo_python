# Ler um número e definir contador
num = int(input('Digite um número:'))
cont = 1
res = 1
# Regra geral
if num == 1 or num == 0:
    print('{}! = 1'.format(num))
# Fatoração
else:
    while cont != num:
        fat = num - cont
        cont += 1
        res *= fat
    print('{}! = {} = {}'.format(num, (num * res)))
print('FIM')
