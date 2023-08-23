# Número por extenso #

num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis',
       'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quatorze', 'quize', 'dezeisseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20:'))
    if 0 <= n <= 20:
        print(f'Você digitou o número {num[n]}.')
    while True:
        r = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
        if r in 'S':
            n = int(input('Digite um número:'))
            print(f'Você digitou número {num[n]}')
        else:
            break
    break
print('Fim do programa.')
