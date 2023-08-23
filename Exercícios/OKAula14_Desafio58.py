# Jogo de adivinha
from random import randint
print('Tente adivinhar um número entre 0 e 10:')
num = randint(0, 10)
jogador = int(input())
cont = 1
while jogador != num:
    cont += 1
    if jogador > num:
        print('Menos...')
        jogador = int(input('Tente novamente:'))
    else:
        print('Mais...')
        jogador = int(input('Tente novamente:'))
    if jogador == num:
        print('Parabéns! Você acertou em {} tentativas.'.format(cont))
print('O número era {}.'.format(num))
print('FIM.')
