# Cadastro de números com insert

num = []
for pos, x in enumerate(range(0, 5)):
    n = int(input('Digite um valor:'))
    if pos == 0 or n > max(num):
        num.append(n)
        print(f'Valor cadastrado na posição {num.index(n)}.')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Valor cadastrado na posição {num.index(n)}')
                break
            pos += 1

print(num)
