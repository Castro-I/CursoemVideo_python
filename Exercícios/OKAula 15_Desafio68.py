# Par ou ímpar
#Importando o módulos e criando a variáveis
from time import sleep
from random import randint

pc = randint(0, 10)
s = cont = 0
#Definindo quem é par ou ímpar e acrescentando algorítmo

while True:
    res = str(input('Deseja ser par ou ímpar?')).upper().strip()
    if res in 'PARIÍMPAR':
        n = int(input('Digite um número:'))
        print('-' * 30)
        s = n + pc
        if s % 2 == 0:
            ganha = 'PAR'
        else:
            ganha = 'ÍMPAR'
        print(f'Eu joguei {pc} e você {n}, que soma {s}.\nEntão', end='')
        print('...')
        sleep(1)
        if res == ganha:
            print('Parbéns, você ganhou!')
            pc = randint(0, 10)
            cont += 1
        else:
            print('Que pena... Você perdeu.')
            print('O jogo acabou')
            if cont > 0:
                print(f'Você ganhou {cont} partidas.')
            break
