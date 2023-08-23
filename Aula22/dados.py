def moedas(n, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


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


def leia_float(comando):
    while True:
        try:
            real = float(input(comando))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: O valor digitado não é válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mO usuário optou por não digitar valor.\033[m')
            return 0
        else:
            return real


def resumo(n, aum=0, dim=0):
    from Aula22 import moeda
    print('_' * 40)
    print(f' {"RESUMO DO VALOR":^40}  ')
    print('_' * 40)
    print(f'Valor analisado:  \t{moedas(n)}')
    print(f'Dobro do valor:  \t{moeda.dobro(n, True)}')
    print(f'Metade do valor:  \t{moeda.metade(n, True)}')
    print(f'{aum}% de aumento:  \t{moeda.aumentar(n, aum, True)}')
    print(f'{dim}% de redução:  \t{moeda.diminuir(n, dim, True)}')
    print('_' * 40)
