# Definindo cores
class Cores:
    vermelho = '\033[0;31m'
    azul = '\033[0;34m'
    verde = '\033[0;32m'
    amarelo = '\033[1;33m'
    branco = ''


# Funções
def leia_int(comando):
    while True:
        try:
            inteiro = int(input(comando))
        except (TypeError, ValueError):
            print(f'\033[0;31mERRO: O valor digitado não é valido\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário optou por não digitar valor.\033[m')
            return 0
        else:
            return inteiro


def linha(cor='', tam=40):
    print(cor, '~' * tam, '\033[m')


def titulo(txt, cor=''):
    linha(cor)
    print(cor, txt.center(40), '\033[m')
    linha(cor)


def menu(*opt, cor):
    for c, v in enumerate(opt):
        print(cor, f'{c + 1}', cor, f'- \t{v}\033[m')
