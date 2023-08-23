#Matriz em python

matriz = [[], [], []]
cont = 0
for n in range(0, 3):
    num = int(input(f'Digite um valor para a posição (0x{cont}):'))
    matriz[0].append(num)
    cont += 1
cont1 = 0
for n1 in range(0, 3):
    num = int(input(f'Digite um valor para a posição (1x{cont1}):'))
    matriz[1].append(num)
    cont1 += 1
cont2 = 0
for n2 in range(0, 3):
    num = int(input(f'Digite um valora para a posição (2x{cont2}):'))
    matriz[2].append(num)
    cont2 += 1
print('=-' * 22)
print(f'''[ {matriz[0][0]} ][ {matriz[0][1]} ][ {matriz[0][2]} ]
[ {matriz[1][0]} ][ {matriz[1][1]} ][ {matriz[1][2]} ]
[ {matriz[2][0]} ][ {matriz[2][1]} ][ {matriz[2][2]} ]''')
#Exercício 87
print('=-' * 22)
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
par = 0
for p in matriz[0]:
    if p % 2 == 0:
        par += p
for p1 in matriz[1]:
    if p1 % 2 == 0:
        par += p1
for p2 in matriz[2]:
    if p2 % 2 == 0:
        par += p2
print(f'O soma dos números pares é igual a {par}')
print(f'A soma do valores da terceira coluna é igual a {matriz[0][2] + matriz[1][2] + matriz[2][2]}')
