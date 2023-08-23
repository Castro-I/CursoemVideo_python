from Aula23_Desafio115.lib.interface import *
from Aula23_Desafio115.lib import Arquivo
from time import sleep

if Arquivo.check_arquivo('cadstro_pessoas.txt'):
    print(Arquivo.criar_aquivo('cadastro_pessoas.txt'))

while True:
    titulo('Menu do Programa', Cores.azul)
    menu('Cadastro', 'Listar pessoas cadastradas', 'Sair do programa', cor=Cores.amarelo)
    linha(Cores.azul)
    r = leia_int('Digite sua opção:')
    if r == 1:
        titulo('Cadastro', Cores.azul)
        Arquivo.cadastro(file='cadastro_pessoas.txt', nome=str(input('Nome:')), idade=str(input('Idade:')))
    elif r == 2:
        titulo('Lista', Cores.azul)
        linha(Cores.amarelo)
        Arquivo.viz_lista(file='cadastro_pessoas.txt')
        linha(Cores.amarelo)
    elif r == 3:
        break
    else:
        print(Cores.vermelho, 'Digite um valor válido.\033[m')
    sleep(1)
titulo('Programa encerrado', Cores.vermelho)
