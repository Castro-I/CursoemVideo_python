# Programa leitor de números#

""" Atribuição de valores"""

n = int(input('Digite um número inteiro:'))
N = [n]
Nsoma = maior = menor = 0
cont = 0

""" Condição de parada"""

resposta = str(input('Quer digitar outro número?').upper())
while resposta in 'SIM':
    n = int(input('Digite outro número inteiro:'))
    N.append(n)
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer digitar outro?').upper())

""" Algóritmo para soma"""
while len(N) != 0:
    Nsoma += N[0]
    N.pop(0)
""" Algóritmo para média"""

media = Nsoma / (cont + 1)

""" Algóritmo para comparar"""

print('''Você digitou {} e a média é igual a {:2f}.
O maior entre eles é {}.
O menor entre eles é {}.'''.format((cont + 1), media, maior, menor))
print('Fim.')
