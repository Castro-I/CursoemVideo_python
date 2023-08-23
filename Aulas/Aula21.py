# Interactive help
help(print)
print(input.__doc__)
"Help() no python console"


# Docstrings
def contador(i, f, p):
    """
    -> Faz uma contagem e mostra na tela:
    :param i:ínicio da contagem
    :param f:fim da contagem
    :param p:passo da contagem
    :return:sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('FIM!')


contador(0, 100, 10)
help(contador)


# Parametros opcionais
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()
