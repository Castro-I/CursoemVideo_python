from random import randint

numeros = list()


# Função
def sorteio():
    for x in range(0, 5):
        numeros.append(randint(0, 10))
    print(f'Os números sorteados foram: {numeros}')


def somapar():
    soma = 0
    npares = list()
    for x in numeros:
        if x % 2 == 0:
            npares.append(x)
            soma += x
    print(f'Os números pares são: {npares} ')
    print(f'e sua soma é igual a {soma}')


# Programa principal
sorteio()
somapar()
