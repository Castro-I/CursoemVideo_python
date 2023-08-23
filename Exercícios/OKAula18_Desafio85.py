#listas com pares e ímpares

numeros = [[], []]
num = 1
for n in range(0, 7):
    v = int(input(f'Digite o {num} número:'))
    if v % 2 == 0:
        numeros[0].append(v)
    elif v % 2 != 0:
        numeros[1].append(v)
    num += 1
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram:{numeros[0]}\nJá os números ímpares foram: {numeros[1]}')
