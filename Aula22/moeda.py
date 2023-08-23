from Aula22 import dados


def dobro(n, form=False):
    if form:
        return dados.moedas(n * 2)
    else:
        return n * 2


def metade(n, form=False):
    if form:
        return dados.moedas(n)
    else:
        return n / 2


def aumentar(n, porctg, form=False):
    if form:
        return dados.moedas(n + (n * (porctg / 100)))
    else:
        return n + (n * (porctg / 100))


def diminuir(n, porctg, form=False):
    if form:
        return dados.moedas(n - (n * (porctg / 100)))
    else:
        return n - (n * (porctg / 100))
