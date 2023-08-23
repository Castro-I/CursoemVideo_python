# Fatorial
def fatorial(num=1, show=False):
    """
    Calculadora de fatorial:
    ---------------------------------
    :param num: Número a ser calculado.
    :param show: (Opcional) Imprime na tela o cálculo.
    :return: retorna o resultado do cálculo.
    """
    c = 1
    print(f'{num}! :', end=' ')
    for n in range(num, 0, -1):
        if show:
            print(f'{n}', end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        c *= n
    return c


print(fatorial(7, True))
print(fatorial.__doc__)
