#Palpites para Mega-Sena

from random import randint
from time import sleep
q_jogos = int(input('Quantos jogos você quer gerar?'))
print('=-' * 10, f'GERANDO {q_jogos} JOGOS', '=-' * 10)


def sorteio():
    num = []
    while len(num) != 6:
        j1 = randint(1, 60)
        while j1 in num:
            j1 = randint(1, 60)
        num.append(j1)
    num.sort()
    print(num)


cont = 1
while q_jogos != 0:
    print(f'Jogo {cont}:', end=' ')
    sorteio()
    sleep(1)
    q_jogos -= 1
    cont += 1
print('=-' * 11, ' BOA SORTE ', '=-' * 11)
