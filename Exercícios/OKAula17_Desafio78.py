# Comparação de valores
num = list([])
for pos, n in enumerate(range(0, 5)):
    num.append(int(input(f'Digite um valor para a posição {pos + 1}:')))
print(f'Você digitou os números: {num}')
print('_' * 40)
print(f'O maior número foi o {max(num)} nas posições:', end=' ')
for i, v in enumerate(num):
    if v ==max(num):
        print(f'{i + 1}...', end='')
print()
print(f'O menor número foi o {min(num)} na posição:', end=' ')
for i, v in enumerate(num):
    if v == min(num):
        print(f'{i + 1}... ', end='')
