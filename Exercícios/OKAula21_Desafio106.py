#Interactive help
def titulo(txt, cor='preto'):
    if cor == 'preto':
        print('\033[0;40m\033' * len(txt))
        print(f'\033[0;40m{txt}\033')
        print('\033[0;40m\033' * len(txt))
    elif cor == 'azul':
        print('\033[0;44m\033' * len(txt))
        print(f'\033[0;44m{txt}\033')
        print('\033[0;44m\033' * len(txt))
    elif cor == 'vermelho':
        print('\033[0;41m~\033' * len(txt))
        print(f'\033[0;41m{txt}\033')
        print('\033[0;41m~\033' * len(txt))


def ajuda():
    from time import sleep
    while True:
        titulo('  SISTEMA DE AJUDA EM PYTHON  ', cor='azul')
        p = str(input('\033[mFunção ou biblioteca > '))
        if p.upper() == 'FIM':
            break
        else:
            titulo(' ANALISANDO SISTEMA  ', cor='preto')
            sleep(0.5)
            print(f'\033[0;39m{help(p)}\033')
            sleep(0.3)
    titulo('ATÉ LOGO.', cor='vermelho')


ajuda()
