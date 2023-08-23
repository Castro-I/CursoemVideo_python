# Programa de soma#

""" Atribuindo valores"""

n = int(input('Digite um número:'))
N = [n]
cont = 1
resultado = 0

""" Estabelencendo condição de parada."""

while n != 999:
    n = int(input('Digite outro número:'))
    if n == 999:
        break
    N.append(n)
    cont += 1

""" Montando algorítmo de soma"""

while len(N) != 0:
    resultado += N[0]
    N.pop(0)

print('Você digitou {} números\nA soma entre eles é igual a {}.'.format(cont, resultado))
print('Fim.')
