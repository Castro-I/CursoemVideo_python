# cadastro de valores
num = []
while True:
    n = int(input('Digite um valor:'))
    if n not in num:
        num.append(n)
        print('Valor cadastrado.')
        print('_' * 30)
        res = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        print('_'* 30)
    elif n in num:
        print('Valor duplicado. Não é possível cadastrar.')
        print('_' * 30)
    else:
        print('Valor inválido.')
        print('_' * 30)
    if res in 'S':
        continue
    elif res in 'N':
        break
print(f'Você digitou os números: {sorted(num)}')
