# Dados de uma lista

num = []
while True:
    n = num.append(int(input('Digite um valor:')))
    print('_' * 30)
    r = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    print('_' * 30)
    if r in 'S':
        continue
    elif r in 'N':
        break
    else:
        r = str(input('Resposta inválida.\nDeseja continuar? [S/N]'))
        print('_' * 30)
print(f'{len(num)} números foram digitados.')
print('_' * 30)
print(f'Lista em ordem decrescente: {sorted(num, reverse= True)}')
print('_' * 30)
if 5 in num:
    print(f'O número 5 foi digitado e está na lista na posição {num.index(5)}.')
else:
    print(' O número 5 não foi digitado, portanto não está na lista.')
