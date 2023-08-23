from Aula23_Desafio115.lib.interface import *


def check_arquivo(nome):
    try:
        with open(nome, 'rt') as arquivo:
            arquivo.close()
    except FileNotFoundError:
        return False


def criar_aquivo(nome):
    try:
        with open(nome, 'at+') as arquivo:
            arquivo.write('')
    except:
        return print(Cores.vermelho, 'Erro ao criar o arquivo.\033[m')
    else:
        return print(f'Arquivo {nome} criado com sucesso!')
    finally:
        arquivo.close()


def cadastro(file, nome, idade):
    try:
        with open(file, 'a') as arquivo:
            arquivo.write(f'{nome:<30}{idade:>3} anos\n')
    except:
        print(Cores.vermelho, 'Erro: Falha na escrita do arquivo.\033[m')
    else:
        return print(Cores.verde, 'Cadastro realizado com sucesso.\033[m')
    finally:
        arquivo.close()


def viz_lista(file):
    try:
        with open(file, "r") as arquivo:
            lista = arquivo.read()
    except:
        print('Erro de leitura.')
    else:
        return print(Cores.branco, f'{lista}\033[m')
    finally:
        arquivo.close()
